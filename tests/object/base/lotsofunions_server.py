# This file was generated by ModelOS
import json
import logging
import os
import typing
from typing import List

import uvicorn
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import BaseRoute, Route

from modelos.object.encoding import deep_isinstance, is_first_order, json_is_type_match

from .base_test import Ham, LotsOfUnions

log_level = os.getenv("LOG_LEVEL")
if log_level is None:
    logging.basicConfig(level=logging.INFO)
else:
    logging.basicConfig(level=log_level)


class LotsOfUnionsServer(LotsOfUnions):
    """A resource server for LotsOfUnions"""

    async def _echo_req(self, request):
        """Request for function:
        echo(self, txt: Optional[str] = None) -> str
        """

        body = await request.body()
        print("len body: ", len(body))
        print("body: ", body)

        _jdict = {}
        if len(body) != 0:
            _jdict = json.loads(body)

        headers = request.headers
        logging.debug(f"headers: {headers}")
        self._check_lock(headers)

        if "txt" in _jdict:
            _txt = _jdict["txt"]
            # code for union: typing.Optional[str]
            if _txt is None:
                pass
            elif type(_txt) == str:
                pass
            else:
                raise ValueError(
                    f"Argument could not be deserialized: txt - type: {type(_txt)}"
                )
            # end union: typing.Optional[str]

            _jdict["txt"] = _txt

        print("calling function: ", _jdict)
        _ret = self.echo(**_jdict)
        print("called function: ", _ret)
        _ret = {"value": _ret}

        print("returning: ", _ret)
        return JSONResponse(_ret)

    async def _health_req(self, request):
        """Request for function:
        health(self) -> Dict[str, str]
        """

        body = await request.body()
        print("len body: ", len(body))
        print("body: ", body)

        _jdict = {}
        if len(body) != 0:
            _jdict = json.loads(body)

        headers = request.headers
        logging.debug(f"headers: {headers}")

        print("calling function: ", _jdict)
        _ret = self.health(**_jdict)
        print("called function: ", _ret)

        print("returning: ", _ret)
        return JSONResponse(_ret)

    async def _info_req(self, request):
        """Request for function:
        info(self) -> modelos.object.kind.ObjectInfo
        """

        body = await request.body()
        print("len body: ", len(body))
        print("body: ", body)

        _jdict = {}
        if len(body) != 0:
            _jdict = json.loads(body)

        headers = request.headers
        logging.debug(f"headers: {headers}")

        print("calling function: ", _jdict)
        _ret = self.info(**_jdict)
        print("called function: ", _ret)
        # code for object: <class 'modelos.object.kind.ObjectInfo'>
        _ret = _ret.__dict__  # type: ignore
        _ext: typing.Optional[typing.Dict[str, str]] = _ret["ext"]
        # code for union: typing.Optional[typing.Dict[str, str]]
        if deep_isinstance(_ext, None):
            pass
        elif deep_isinstance(_ext, typing.Dict[str, str]):
            pass
        else:
            raise ValueError(
                "Do not know how to serialize"
                + "parameter 'typing.Optional[typing.Dict[str, str]]' "
                + f"of type '{type(_ext)}'"
            )
        # end union: typing.Optional[typing.Dict[str, str]]

        _ret["ext"] = _ext
        # end object: <class 'modelos.object.kind.ObjectInfo'>

        print("returning: ", _ret)
        return JSONResponse(_ret)

    async def _lock_req(self, request):
        """Request for function:
        lock(self, key: Optional[str] = None, timeout: Optional[int] = None) -> None  # noqa
        """

        body = await request.body()
        print("len body: ", len(body))
        print("body: ", body)

        _jdict = {}
        if len(body) != 0:
            _jdict = json.loads(body)

        headers = request.headers
        logging.debug(f"headers: {headers}")

        if "key" in _jdict:
            _key = _jdict["key"]
            # code for union: typing.Optional[str]
            if _key is None:
                pass
            elif type(_key) == str:
                pass
            else:
                raise ValueError(
                    f"Argument could not be deserialized: key - type: {type(_key)}"
                )
            # end union: typing.Optional[str]

            _jdict["key"] = _key
        if "timeout" in _jdict:
            _timeout = _jdict["timeout"]
            # code for union: typing.Optional[int]
            if _timeout is None:
                pass
            elif type(_timeout) == int:
                pass
            else:
                raise ValueError(
                    f"Argument could not be deserialized: timeout - type: {type(_timeout)}"
                )
            # end union: typing.Optional[int]

            _jdict["timeout"] = _timeout

        print("calling function: ", _jdict)
        _ret = self.lock(**_jdict)
        print("called function: ", _ret)
        _ret = {"value": None}

        print("returning: ", _ret)
        return JSONResponse(_ret)

    async def _optional_lists_req(self, request):
        """Request for function:
        optional_lists(self, y: Union[List[__main__.Ham], Dict[str, __main__.Ham]], as_dict: bool = True) -> Union[List[__main__.Ham], Dict[str, __main__.Ham]]  # noqa
        """

        body = await request.body()
        print("len body: ", len(body))
        print("body: ", body)

        _jdict = {}
        if len(body) != 0:
            _jdict = json.loads(body)

        headers = request.headers
        logging.debug(f"headers: {headers}")
        self._check_lock(headers)

        _y = _jdict["y"]
        # code for union: typing.Union[typing.List[Ham], typing.Dict[str, Ham]]
        if json_is_type_match(typing.List[Ham], _y):
            print("checking type match match for typing.List")
            _y = _jdict["y"]
            # code for list: typing.List[Ham]
            if not json_is_type_match(typing.List[Ham], _y):
                raise ValueError(
                    "JSON from 'y' returned does not match type: typing.List[__main__.Ham]"
                )

            _y_list: typing.List[Ham] = []
            for _a_val in _y:
                # code for obj: Ham
                _a_val_obj = object.__new__(Ham)
                _a_attr = _a_val["a"]
                setattr(_a_val_obj, "a", _a_attr)

                _b_attr = _a_val["b"]
                setattr(_a_val_obj, "b", _b_attr)

                _a_val = _a_val_obj  # type: ignore
                # end obj: Ham

                _y_list.append(_a_val)  # type: ignore
            _y = _y_list
            # end list: typing.List[Ham]

            _jdict["y"] = _y
        elif json_is_type_match(typing.Dict[str, Ham], _y):
            print("checking type match match for typing.Dict")
            _y = _jdict["y"]
            # code for dict: typing.Dict[str, Ham]
            if not json_is_type_match(typing.Dict[str, Ham], _y):
                raise ValueError(
                    "JSON from 'y' returned does not match type: typing.Dict[str, __main__.Ham]"
                )

            _y_dict: typing.Dict[str, Ham] = {}
            for _b_key, _c_val in _y.items():
                # code for obj: Ham
                _c_val_obj = object.__new__(Ham)
                _a_attr = _c_val["a"]
                setattr(_c_val_obj, "a", _a_attr)

                _b_attr = _c_val["b"]
                setattr(_c_val_obj, "b", _b_attr)

                _c_val = _c_val_obj  # type: ignore
                # end obj: Ham

                _y_dict[_b_key] = _c_val  # type: ignore
            _y = _y_dict
            # end dict: typing.Dict[str, Ham]

            _jdict["y"] = _y
        else:
            raise ValueError(
                f"Argument could not be deserialized: y - type: {type(_y)}"
            )
        # end union: typing.Union[typing.List[Ham], typing.Dict[str, Ham]]

        _jdict["y"] = _y

        print("calling function: ", _jdict)
        _ret = self.optional_lists(**_jdict)
        print("called function: ", _ret)
        # code for union: typing.Union[typing.List[__main__.Ham], typing.Dict[str, __main__.Ham]]
        if deep_isinstance(_ret, typing.List[Ham]):
            # code for list: typing.List[__main__.Ham]
            _ret_list = []
            for _d_val in _ret:  # type: ignore
                # code for object: <class '__main__.Ham'>
                _d_val = _d_val.__dict__  # type: ignore
                # end object: <class '__main__.Ham'>

                _ret_list.append(_d_val)
            _ret = _ret_list
            # end list: typing.List[__main__.Ham]

        elif deep_isinstance(_ret, typing.Dict[str, Ham]):
            # code for dict arg: typing.Dict[str, __main__.Ham]
            _ret_dict = {}
            for _e_key, _f_val in _ret.items():  # type: ignore
                # code for object: <class '__main__.Ham'>
                _f_val = _f_val.__dict__  # type: ignore
                # end object: <class '__main__.Ham'>

                _ret_dict[_e_key] = _f_val  # type: ignore
            _ret = _ret_dict
            # end dict: typing.Dict[str, __main__.Ham]

        else:
            raise ValueError(
                "Do not know how to serialize"
                + "parameter 'typing.Union[typing.List[__main__.Ham], typing.Dict[str, __main__.Ham]]' "
                + f"of type '{type(_ret)}'"
            )
        # end union: typing.Union[typing.List[__main__.Ham], typing.Dict[str, __main__.Ham]]

        if is_first_order(type(_ret)) or _ret is None:
            _ret = {"value": _ret}

        print("returning: ", _ret)
        return JSONResponse(_ret)

    async def _optional_obj_req(self, request):
        """Request for function:
        optional_obj(self, h: Union[__main__.Ham, Dict[str, Any]], return_dict: Optional[bool] = None) -> Union[__main__.Ham, Dict[str, Any]]  # noqa
        """

        body = await request.body()
        print("len body: ", len(body))
        print("body: ", body)

        _jdict = {}
        if len(body) != 0:
            _jdict = json.loads(body)

        headers = request.headers
        logging.debug(f"headers: {headers}")
        self._check_lock(headers)

        _h = _jdict["h"]
        # code for union: typing.Union[Ham, typing.Dict[str, typing.Any]]
        if json_is_type_match(Ham, _h):
            print("checking type match match for Ham")
            _h = _jdict["h"]

            # code for obj: Ham
            _h_obj = object.__new__(Ham)
            _a_attr = _h["a"]
            setattr(_h_obj, "a", _a_attr)

            _b_attr = _h["b"]
            setattr(_h_obj, "b", _b_attr)

            _h = _h_obj  # type: ignore
            # end obj: Ham

            _jdict["h"] = _h
        elif json_is_type_match(typing.Dict[str, typing.Any], _h):
            print("checking type match match for typing.Dict")
            _h = _jdict["h"]
            # code for dict: typing.Dict[str, typing.Any]
            if not json_is_type_match(typing.Dict[str, typing.Any], _h):
                raise ValueError(
                    "JSON from 'h' returned does not match type: typing.Dict[str, typing.Any]"
                )

            _h_dict: typing.Dict[str, typing.Any] = {}
            for _a_key, _b_val in _h.items():
                _h_dict[_a_key] = _b_val  # type: ignore
            _h = _h_dict
            # end dict: typing.Dict[str, typing.Any]

            _jdict["h"] = _h
        else:
            raise ValueError(
                f"Argument could not be deserialized: h - type: {type(_h)}"
            )
        # end union: typing.Union[Ham, typing.Dict[str, typing.Any]]

        _jdict["h"] = _h
        if "return_dict" in _jdict:
            _return_dict = _jdict["return_dict"]
            # code for union: typing.Optional[bool]
            if _return_dict is None:
                pass
            elif type(_return_dict) == bool:
                pass
            else:
                raise ValueError(
                    f"Argument could not be deserialized: return_dict - type: {type(_return_dict)}"
                )
            # end union: typing.Optional[bool]

            _jdict["return_dict"] = _return_dict

        print("calling function: ", _jdict)
        _ret = self.optional_obj(**_jdict)
        print("called function: ", _ret)
        # code for union: typing.Union[__main__.Ham, typing.Dict[str, typing.Any]]
        if deep_isinstance(_ret, Ham):
            # code for object: <class '__main__.Ham'>
            _ret = _ret.__dict__  # type: ignore
            # end object: <class '__main__.Ham'>

        elif deep_isinstance(_ret, typing.Dict[str, typing.Any]):
            # code for dict arg: typing.Dict[str, typing.Any]
            _ret_dict = {}
            for _c_key, _d_val in _ret.items():  # type: ignore
                _ret_dict[_c_key] = _d_val  # type: ignore
            _ret = _ret_dict
            # end dict: typing.Dict[str, typing.Any]

        else:
            raise ValueError(
                "Do not know how to serialize"
                + "parameter 'typing.Union[__main__.Ham, typing.Dict[str, typing.Any]]' "
                + f"of type '{type(_ret)}'"
            )
        # end union: typing.Union[__main__.Ham, typing.Dict[str, typing.Any]]

        if is_first_order(type(_ret)) or _ret is None:
            _ret = {"value": _ret}

        print("returning: ", _ret)
        return JSONResponse(_ret)

    async def _optional_tuples_req(self, request):
        """Request for function:
        optional_tuples(self, x: Union[Tuple[str, __main__.Ham], Dict[str, __main__.Ham]]) -> Union[Tuple[str, __main__.Ham], Dict[str, __main__.Ham]]  # noqa
        """

        body = await request.body()
        print("len body: ", len(body))
        print("body: ", body)

        _jdict = {}
        if len(body) != 0:
            _jdict = json.loads(body)

        headers = request.headers
        logging.debug(f"headers: {headers}")
        self._check_lock(headers)

        _x = _jdict["x"]
        # code for union: typing.Union[typing.Tuple[str, Ham], typing.Dict[str, Ham]]
        if json_is_type_match(typing.Tuple[str, Ham], _x):
            print("checking type match match for typing.Tuple")
            _x = _jdict["x"]
            # code for tuple: typing.Tuple[str, Ham]
            _x_tuple: typing.Tuple[str, Ham] = ()  # type: ignore

            # code for tuple arg: <class 'str'>
            _x_0 = _x[0]
            _x_tuple = _x_tuple + (_x_0,)  # type: ignore
            # end tuple arg: <class 'str'>

            # code for tuple arg: <class '__main__.Ham'>
            _x_1 = _x[1]

            # code for obj: Ham
            _x_1_obj = object.__new__(Ham)
            _a_attr = _x_1["a"]
            setattr(_x_1_obj, "a", _a_attr)

            _b_attr = _x_1["b"]
            setattr(_x_1_obj, "b", _b_attr)

            _x_1 = _x_1_obj  # type: ignore
            # end obj: Ham

            _x_tuple = _x_tuple + (_x_1,)  # type: ignore
            # end tuple arg: <class '__main__.Ham'>

            _x = _x_tuple  # type: ignore
            # end tuple: typing.Tuple[str, Ham]

            _jdict["x"] = _x
        elif json_is_type_match(typing.Dict[str, Ham], _x):
            print("checking type match match for typing.Dict")
            _x = _jdict["x"]
            # code for dict: typing.Dict[str, Ham]
            if not json_is_type_match(typing.Dict[str, Ham], _x):
                raise ValueError(
                    "JSON from 'x' returned does not match type: typing.Dict[str, __main__.Ham]"
                )

            _x_dict: typing.Dict[str, Ham] = {}
            for _a_key, _b_val in _x.items():
                # code for obj: Ham
                _b_val_obj = object.__new__(Ham)
                _a_attr = _b_val["a"]
                setattr(_b_val_obj, "a", _a_attr)

                _b_attr = _b_val["b"]
                setattr(_b_val_obj, "b", _b_attr)

                _b_val = _b_val_obj  # type: ignore
                # end obj: Ham

                _x_dict[_a_key] = _b_val  # type: ignore
            _x = _x_dict
            # end dict: typing.Dict[str, Ham]

            _jdict["x"] = _x
        else:
            raise ValueError(
                f"Argument could not be deserialized: x - type: {type(_x)}"
            )
        # end union: typing.Union[typing.Tuple[str, Ham], typing.Dict[str, Ham]]

        _jdict["x"] = _x

        print("calling function: ", _jdict)
        _ret = self.optional_tuples(**_jdict)
        print("called function: ", _ret)
        # code for union: typing.Union[typing.Tuple[str, __main__.Ham], typing.Dict[str, __main__.Ham]]
        if deep_isinstance(_ret, typing.Tuple[str, Ham]):
            # code for tuple: typing.Tuple[str, __main__.Ham]
            _ret_list = []
            # code for tuple arg: <class 'str'>
            _ret_0 = _ret[0]
            _ret_list.append(_ret_0)  # type: ignore
            # end tuple arg: <class 'str'>

            # code for tuple arg: <class '__main__.Ham'>
            _ret_1 = _ret[1]
            # code for object: <class '__main__.Ham'>
            _ret_1 = _ret_1.__dict__  # type: ignore
            # end object: <class '__main__.Ham'>

            _ret_list.append(_ret_1)  # type: ignore
            # end tuple arg: <class '__main__.Ham'>

            _ret = _ret_list  # type: ignore
            # end tuple: typing.Tuple[str, __main__.Ham]

        elif deep_isinstance(_ret, typing.Dict[str, Ham]):
            # code for dict arg: typing.Dict[str, __main__.Ham]
            _ret_dict = {}
            for _c_key, _d_val in _ret.items():  # type: ignore
                # code for object: <class '__main__.Ham'>
                _d_val = _d_val.__dict__  # type: ignore
                # end object: <class '__main__.Ham'>

                _ret_dict[_c_key] = _d_val  # type: ignore
            _ret = _ret_dict
            # end dict: typing.Dict[str, __main__.Ham]

        else:
            raise ValueError(
                "Do not know how to serialize"
                + "parameter 'typing.Union[typing.Tuple[str, __main__.Ham], typing.Dict[str, __main__.Ham]]' "
                + f"of type '{type(_ret)}'"
            )
        # end union: typing.Union[typing.Tuple[str, __main__.Ham], typing.Dict[str, __main__.Ham]]

        if is_first_order(type(_ret)) or _ret is None:
            _ret = {"value": _ret}

        print("returning: ", _ret)
        return JSONResponse(_ret)

    async def _returns_optional_req(self, request):
        """Request for function:
        returns_optional(self, a: Union[str, int]) -> Optional[str]
        """

        body = await request.body()
        print("len body: ", len(body))
        print("body: ", body)

        _jdict = {}
        if len(body) != 0:
            _jdict = json.loads(body)

        headers = request.headers
        logging.debug(f"headers: {headers}")
        self._check_lock(headers)

        _a = _jdict["a"]
        # code for union: typing.Union[str, int]
        if type(_a) == str:
            pass
        elif type(_a) == int:
            pass
        else:
            raise ValueError(
                f"Argument could not be deserialized: a - type: {type(_a)}"
            )
        # end union: typing.Union[str, int]

        _jdict["a"] = _a

        print("calling function: ", _jdict)
        _ret = self.returns_optional(**_jdict)
        print("called function: ", _ret)
        # code for union: typing.Optional[str]
        if deep_isinstance(_ret, None):
            pass
        elif deep_isinstance(_ret, str):
            pass
        else:
            raise ValueError(
                "Do not know how to serialize"
                + "parameter 'typing.Optional[str]' "
                + f"of type '{type(_ret)}'"
            )
        # end union: typing.Optional[str]

        if is_first_order(type(_ret)) or _ret is None:
            _ret = {"value": _ret}

        print("returning: ", _ret)
        return JSONResponse(_ret)

    async def _save_req(self, request):
        """Request for function:
        save(self, out_dir: str = './artifacts') -> None
        """

        body = await request.body()
        print("len body: ", len(body))
        print("body: ", body)

        _jdict = {}
        if len(body) != 0:
            _jdict = json.loads(body)

        headers = request.headers
        logging.debug(f"headers: {headers}")
        self._check_lock(headers)

        print("calling function: ", _jdict)
        _ret = self.save(**_jdict)
        print("called function: ", _ret)
        _ret = {"value": None}

        print("returning: ", _ret)
        return JSONResponse(_ret)

    async def _unlock_req(self, request):
        """Request for function:
        unlock(self, key: Optional[str] = None, force: bool = False) -> None
        """

        body = await request.body()
        print("len body: ", len(body))
        print("body: ", body)

        _jdict = {}
        if len(body) != 0:
            _jdict = json.loads(body)

        headers = request.headers
        logging.debug(f"headers: {headers}")

        if "key" in _jdict:
            _key = _jdict["key"]
            # code for union: typing.Optional[str]
            if _key is None:
                pass
            elif type(_key) == str:
                pass
            else:
                raise ValueError(
                    f"Argument could not be deserialized: key - type: {type(_key)}"
                )
            # end union: typing.Optional[str]

            _jdict["key"] = _key

        print("calling function: ", _jdict)
        _ret = self.unlock(**_jdict)
        print("called function: ", _ret)
        _ret = {"value": None}

        print("returning: ", _ret)
        return JSONResponse(_ret)

    async def _labels_req(self, request):
        """Request for function:
        labels() -> Dict[str, str]
        """

        body = await request.body()
        print("len body: ", len(body))
        print("body: ", body)

        _jdict = {}
        if len(body) != 0:
            _jdict = json.loads(body)

        headers = request.headers
        logging.debug(f"headers: {headers}")
        self._check_lock(headers)

        print("calling function: ", _jdict)
        _ret = self.labels(**_jdict)
        print("called function: ", _ret)

        print("returning: ", _ret)
        return JSONResponse(_ret)

    async def _name_req(self, request):
        """Request for function:
        name() -> str
        """

        body = await request.body()
        print("len body: ", len(body))
        print("body: ", body)

        _jdict = {}
        if len(body) != 0:
            _jdict = json.loads(body)

        headers = request.headers
        logging.debug(f"headers: {headers}")
        self._check_lock(headers)

        print("calling function: ", _jdict)
        _ret = self.name(**_jdict)
        print("called function: ", _ret)
        _ret = {"value": _ret}

        print("returning: ", _ret)
        return JSONResponse(_ret)

    async def _short_name_req(self, request):
        """Request for function:
        short_name() -> str
        """

        body = await request.body()
        print("len body: ", len(body))
        print("body: ", body)

        _jdict = {}
        if len(body) != 0:
            _jdict = json.loads(body)

        headers = request.headers
        logging.debug(f"headers: {headers}")
        self._check_lock(headers)

        print("calling function: ", _jdict)
        _ret = self.short_name(**_jdict)
        print("called function: ", _ret)
        _ret = {"value": _ret}

        print("returning: ", _ret)
        return JSONResponse(_ret)

    def _routes(self) -> List[BaseRoute]:
        return [
            Route("/echo", endpoint=self._echo_req, methods=["POST"]),
            Route("/health", endpoint=self._health_req, methods=["GET", "POST"]),
            Route("/info", endpoint=self._info_req, methods=["POST"]),
            Route("/lock", endpoint=self._lock_req, methods=["POST"]),
            Route(
                "/optional_lists", endpoint=self._optional_lists_req, methods=["POST"]
            ),
            Route("/optional_obj", endpoint=self._optional_obj_req, methods=["POST"]),
            Route(
                "/optional_tuples", endpoint=self._optional_tuples_req, methods=["POST"]
            ),
            Route(
                "/returns_optional",
                endpoint=self._returns_optional_req,
                methods=["POST"],
            ),
            Route("/save", endpoint=self._save_req, methods=["POST"]),
            Route("/unlock", endpoint=self._unlock_req, methods=["POST"]),
            Route("/labels", endpoint=self._labels_req, methods=["POST"]),
            Route("/name", endpoint=self._name_req, methods=["POST"]),
            Route("/short_name", endpoint=self._short_name_req, methods=["POST"]),
        ]


o = LotsOfUnionsServer.from_env()
pkgs = o._reload_dirs()

app = Starlette(routes=o._routes())

if __name__ == "__main__":
    logging.info(f"starting server version '{o.scm.sha()}' on port: 8080")
    uvicorn.run(
        "__main__:app",
        host="0.0.0.0",
        port=8080,
        log_level="info",
        workers=1,
        reload=True,
        reload_dirs=pkgs.keys(),
    )
