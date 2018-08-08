import json
import os
import time

CACHE_TIME = 'time'

CACHE_SPEC = 'spec'

MODEL_NAME_FIELD = 'modelName'
URL_FIELD = 'url'
METHOD_FIELD = 'method'
PARAMETERS_FIELD = 'parameters'

PATHS = 'paths'
OPERATION_ID = 'operationId'
FILE_MODEL_NAME = '_File'
SUCCESS_RESPONSE_CODE = '200'
BASE_PATH = 'basePath'
DEFINITIONS = 'definitions'
OPERATIONS = 'operations'
SCHEMA = 'schema'
MODELS = 'models'
REF = '$ref'
ALL_OF = 'allOf'


class HttpMethod:
    GET = 'get'
    POST = 'post'
    PUT = 'put'


class FdmSwaggerParser:
    _definitions = None

    def pars_spec(self, spec):
        self._definitions = spec[DEFINITIONS]
        _config = {
            MODELS: self._definitions,
            OPERATIONS: self._get_operations(spec)
        }
        return _config

    def _get_operations(self, spec):
        _base_path = spec[BASE_PATH]
        _paths_dict = spec[PATHS]
        _operations_dict = {}
        for _url, _operation_params in list(_paths_dict.items()):
            for _method, _params in list(_operation_params.items()):
                _operation = {
                    METHOD_FIELD: _method,
                    URL_FIELD: _base_path + _url,
                    MODEL_NAME_FIELD: self._get_model_name(_method, _params)
                }
                if PARAMETERS_FIELD in _params:
                    _operation[PARAMETERS_FIELD] = self._get_rest_params(_params[PARAMETERS_FIELD])

                _operation_id = _params[OPERATION_ID]
                _operations_dict[_operation_id] = _operation
        return _operations_dict

    def _get_model_name(self, _method, _params):
        if _method == HttpMethod.GET:
            return self._get_model_name_from_responses(_params)
        elif _method == HttpMethod.POST or _method == HttpMethod.PUT:
            return self._get_model_name_for_post_put_requests(_params)
        else:
            return None

    def _get_model_name_for_post_put_requests(self, params):
        model_name = None
        if PARAMETERS_FIELD in params:
            _body_param_dict = self._get_body_param_form_parameters(params[PARAMETERS_FIELD])
            if _body_param_dict:
                _schema_ref = _body_param_dict[SCHEMA][REF]
                model_name = self._get_model_name_by_schema_ref(_schema_ref)
        if model_name is None:
            model_name = self._get_model_name_from_responses(params)
        return model_name

    @staticmethod
    def _get_body_param_form_parameters(params):
        for param in params:
            if param['in'] == 'body':
                return param

    def _get_model_name_from_responses(self, params):
        _responses = params['responses']
        if SUCCESS_RESPONSE_CODE in _responses:
            response = _responses[SUCCESS_RESPONSE_CODE][SCHEMA]
            if REF in response:
                return self._get_model_name_by_schema_ref(response[REF])
            elif 'properties' in response:
                ref = response['properties']['items']['items'][REF]
                return self._get_model_name_by_schema_ref(ref)
            elif ('type' in response) and response['type'] == "file":
                return FILE_MODEL_NAME
        else:
            return None

    def _get_rest_params(self, params):
        path = {}
        query = {}
        _param = {
            'path': path,
            'query': query
        }
        for param in params:
            in_parm = param['in']
            if in_parm == 'query':
                query[param['name']] = self._simplify_param_def(param)
            elif in_parm == 'path':
                path[param['name']] = self._simplify_param_def(param)
        return _param

    @staticmethod
    def _simplify_param_def(param):
        return {
            'type': param['type'],
            'required': param['required']
        }

    def _get_model_name_by_schema_ref(self, _schema_ref):
        model_name = self._get_model_name_from_url(_schema_ref)
        model_def = self._definitions[model_name]
        if ALL_OF in model_def:
            return self._get_model_name_by_schema_ref(model_def[ALL_OF][0][REF])
        else:
            return model_name

    @staticmethod
    def _get_model_name_from_url(_schema_ref):
        _path = _schema_ref.split('/')
        return _path[len(_path) - 1]


class FdmSwaggerClient:
    __config = None
    PATH_TO_API_SPEC = '/apispec/ngfw.json'

    def __init__(self, conn, cache_file_path=None, cache_expiration_time=0):
        self._conn = conn

        self._cache_expiration_time = cache_expiration_time
        self._cache_file_path = cache_file_path

        if cache_file_path:
            self.__config = self.get_config_from_cache()

        if not self.__config:
            self.__config = self.get_spec_from_server()

    def get_operations(self):
        return self.__config[OPERATIONS]

    def get_operation(self, operation_name):
        return self.get_operations().get(operation_name, None)

    def get_models(self):
        return self.__config[MODELS]

    def get_model(self, model_name):
        return self.get_models().get(model_name, None)

    def get_config_from_cache(self):
        try:
            file_path = self._get_cache_file_path()
            if file_path and self._cache_expiration_time and os.path.exists(file_path):
                with open(file_path) as f:
                    data = json.load(f)
                    if CACHE_TIME in data:
                        if (int(time.time()) - data[CACHE_TIME]) < self._cache_expiration_time:
                            return data[CACHE_SPEC]
                        else:
                            self.clean_cache()
            return None
        except Exception:
            return None

    def clean_cache(self):
        file_path = self._get_cache_file_path()
        if file_path and os.path.exists(file_path):
            os.remove(file_path)

    def _get_cache_file_path(self):
        # TODO:2018-08-08:alexander.vorkov: add host to the file name
        return self._cache_file_path

    def get_spec_from_server(self):
        data = self._conn.send_request(url_path=self.PATH_TO_API_SPEC)
        spec = FdmSwaggerParser().pars_spec(data)
        self._cache_spec(spec)
        return spec

    def _cache_spec(self, spec):
        file_path = self._get_cache_file_path()
        if file_path and self._cache_expiration_time:
            directory = os.path.dirname(file_path)

            if not os.path.exists(directory):
                os.makedirs(directory)

            with open(file_path, 'w') as outfile:
                json.dump({
                    CACHE_TIME: int(time.time()),
                    CACHE_SPEC: spec
                }, outfile)
                return True
        return False