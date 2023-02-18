# This file was generated by ModelOS
import json
import os
import typing
from pathlib import Path
from typing import Type
from urllib import parse, request

from lib_programname import get_path_executed_script

import modelos.object.kind
from modelos import Client
from modelos.object.encoding import deep_isinstance, json_is_type_match
from modelos.object.opts import Opts, OptsBuilder

from .base_test import Ham

if get_path_executed_script() == Path(os.path.dirname(__file__)).joinpath(
    Path("base_test.py")
):
    from __main__ import Ham


class DataClient(Client):
    """A resource client for Data"""

    uri: str = "aunum/mdl-test:data-3967177-7f16fe3"

    def __init__(
        self,
        h: Ham,
        d: typing.Dict[str, Ham],
        lh: typing.List[Ham],
        u: typing.Union[str, Ham],
        o: typing.Optional[Ham] = None,
        **kwargs,
    ) -> None:
        ClientOpts = OptsBuilder[Opts].build(self.__class__)
        opts = ClientOpts(h=h, d=d, lh=lh, u=u, o=o)
        super().__init__(opts=opts, **kwargs)

    def get_d(self, name: str) -> Ham:
        _params = json.dumps({"name": name}).encode("utf8")
        _headers = {"content-type": "application/json", "client-uuid": str(self.uid)}
        _req = request.Request(
            f"{self.server_addr}/get_d",
            data=_params,
            headers=_headers,
        )
        _resp = request.urlopen(_req)
        _data = _resp.read().decode("utf-8")
        _jdict = json.loads(_data)

        if _jdict is None:
            raise ValueError("recieved invalid response from server, check server logs")

        if "value" in _jdict:
            _jdict = _jdict["value"]

        _ret: Ham
        # code for object: <class '__main__.Ham'>
        if not json_is_type_match(Ham, _jdict):
            raise ValueError("JSON returned does not match type: Ham")
        _ret_obj = object.__new__(Ham)  # type: ignore
        _a = _jdict["a"]
        setattr(_ret_obj, "a", _a)

        _b = _jdict["b"]
        setattr(_ret_obj, "b", _b)

        _ret = _ret_obj
        # end object: <class '__main__.Ham'>

        return _ret

    def get_h(self) -> Ham:
        _params = json.dumps({}).encode("utf8")
        _headers = {"content-type": "application/json", "client-uuid": str(self.uid)}
        _req = request.Request(
            f"{self.server_addr}/get_h",
            data=_params,
            headers=_headers,
        )
        _resp = request.urlopen(_req)
        _data = _resp.read().decode("utf-8")
        _jdict = json.loads(_data)

        if _jdict is None:
            raise ValueError("recieved invalid response from server, check server logs")

        if "value" in _jdict:
            _jdict = _jdict["value"]

        _ret: Ham
        # code for object: <class '__main__.Ham'>
        if not json_is_type_match(Ham, _jdict):
            raise ValueError("JSON returned does not match type: Ham")
        _ret_obj = object.__new__(Ham)  # type: ignore
        _a = _jdict["a"]
        setattr(_ret_obj, "a", _a)

        _b = _jdict["b"]
        setattr(_ret_obj, "b", _b)

        _ret = _ret_obj
        # end object: <class '__main__.Ham'>

        return _ret

    def get_lh(self) -> typing.List[Ham]:
        _params = json.dumps({}).encode("utf8")
        _headers = {"content-type": "application/json", "client-uuid": str(self.uid)}
        _req = request.Request(
            f"{self.server_addr}/get_lh",
            data=_params,
            headers=_headers,
        )
        _resp = request.urlopen(_req)
        _data = _resp.read().decode("utf-8")
        _jdict = json.loads(_data)

        if _jdict is None:
            raise ValueError("recieved invalid response from server, check server logs")

        if "value" in _jdict:
            _jdict = _jdict["value"]

        _ret: typing.List[Ham]
        # code for arg: typing.List[__main__.Ham]
        _b_list: typing.List = []
        for _a_val in _jdict:
            # code for object: <class '__main__.Ham'>
            if not json_is_type_match(Ham, _a_val):
                raise ValueError("JSON returned does not match type: Ham")
            _b_obj = object.__new__(Ham)  # type: ignore
            _a = _a_val["a"]
            setattr(_b_obj, "a", _a)

            _b = _a_val["b"]
            setattr(_b_obj, "b", _b)

            _b = _b_obj
            # end object: <class '__main__.Ham'>

            _b_list.append(_b)
        _ret = _b_list
        # end list: typing.List[__main__.Ham]

        return _ret

    def get_o(self) -> typing.Optional[Ham]:
        _params = json.dumps({}).encode("utf8")
        _headers = {"content-type": "application/json", "client-uuid": str(self.uid)}
        _req = request.Request(
            f"{self.server_addr}/get_o",
            data=_params,
            headers=_headers,
        )
        _resp = request.urlopen(_req)
        _data = _resp.read().decode("utf-8")
        _jdict = json.loads(_data)

        if _jdict is None:
            raise ValueError("recieved invalid response from server, check server logs")

        if "value" in _jdict:
            _jdict = _jdict["value"]

        _ret: typing.Optional[Ham]
        # code for union: typing.Optional[__main__.Ham]
        if json_is_type_match(Ham, _jdict):
            # code for object: <class '__main__.Ham'>
            if not json_is_type_match(Ham, _jdict):
                raise ValueError("JSON returned does not match type: Ham")
            _ret_obj = object.__new__(Ham)  # type: ignore
            _a = _jdict["a"]
            setattr(_ret_obj, "a", _a)

            _b = _jdict["b"]
            setattr(_ret_obj, "b", _b)

            _ret = _ret_obj
            # end object: <class '__main__.Ham'>

        elif json_is_type_match(None, _jdict):
            _ret = _jdict
        else:
            raise ValueError(f"Unable to deserialize return value: {type(_jdict)}")
        # end union: typing.Optional[__main__.Ham]

        return _ret

    def get_u(self) -> typing.Union[str, Ham]:
        _params = json.dumps({}).encode("utf8")
        _headers = {"content-type": "application/json", "client-uuid": str(self.uid)}
        _req = request.Request(
            f"{self.server_addr}/get_u",
            data=_params,
            headers=_headers,
        )
        _resp = request.urlopen(_req)
        _data = _resp.read().decode("utf-8")
        _jdict = json.loads(_data)

        if _jdict is None:
            raise ValueError("recieved invalid response from server, check server logs")

        if "value" in _jdict:
            _jdict = _jdict["value"]

        _ret: typing.Union[str, Ham]
        # code for union: typing.Union[str, __main__.Ham]
        if json_is_type_match(str, _jdict):
            _ret = _jdict
        elif json_is_type_match(Ham, _jdict):
            # code for object: <class '__main__.Ham'>
            if not json_is_type_match(Ham, _jdict):
                raise ValueError("JSON returned does not match type: Ham")
            _ret_obj = object.__new__(Ham)  # type: ignore
            _a = _jdict["a"]
            setattr(_ret_obj, "a", _a)

            _b = _jdict["b"]
            setattr(_ret_obj, "b", _b)

            _ret = _ret_obj
            # end object: <class '__main__.Ham'>

        else:
            raise ValueError(f"Unable to deserialize return value: {type(_jdict)}")
        # end union: typing.Union[str, __main__.Ham]

        return _ret

    def health(self) -> typing.Dict[str, str]:
        """Health of the resource

        Returns:
            Dict[str, Any]: Resource health
        """

        _params = json.dumps({}).encode("utf8")
        _headers = {"content-type": "application/json", "client-uuid": str(self.uid)}
        _req = request.Request(
            f"{self.server_addr}/health",
            data=_params,
            headers=_headers,
        )
        _resp = request.urlopen(_req)
        _data = _resp.read().decode("utf-8")
        _jdict = json.loads(_data)

        if _jdict is None:
            raise ValueError("recieved invalid response from server, check server logs")

        if "value" in _jdict:
            _jdict = _jdict["value"]

        _ret: typing.Dict[str, str]
        # code for arg: typing.Dict[str, str]
        if not json_is_type_match(typing.Dict[str, str], _jdict):
            raise ValueError("JSON returned does not match type: typing.Dict[str, str]")
        _ret = _jdict
        # end dict: typing.Dict[str, str]

        return _ret

    def info(self) -> modelos.object.kind.ObjectInfo:
        """Info about the resource

        Returns:
            Dict[str, Any]: Resource info
        """

        _params = json.dumps({}).encode("utf8")
        _headers = {"content-type": "application/json", "client-uuid": str(self.uid)}
        _req = request.Request(
            f"{self.server_addr}/info",
            data=_params,
            headers=_headers,
        )
        _resp = request.urlopen(_req)
        _data = _resp.read().decode("utf-8")
        _jdict = json.loads(_data)

        if _jdict is None:
            raise ValueError("recieved invalid response from server, check server logs")

        if "value" in _jdict:
            _jdict = _jdict["value"]

        _ret: modelos.object.kind.ObjectInfo
        # code for object: <class 'modelos.object.kind.ObjectInfo'>
        if not json_is_type_match(modelos.object.kind.ObjectInfo, _jdict):
            raise ValueError(
                "JSON returned does not match type: modelos.object.kind.ObjectInfo"
            )
        _ret_obj = object.__new__(modelos.object.kind.ObjectInfo)  # type: ignore
        _name = _jdict["name"]
        setattr(_ret_obj, "name", _name)

        _version = _jdict["version"]
        setattr(_ret_obj, "version", _version)

        _env_sha = _jdict["env_sha"]
        setattr(_ret_obj, "env_sha", _env_sha)

        _uri = _jdict["uri"]
        setattr(_ret_obj, "uri", _uri)

        _server_entrypoint = _jdict["server_entrypoint"]
        setattr(_ret_obj, "server_entrypoint", _server_entrypoint)

        _locked = _jdict["locked"]
        setattr(_ret_obj, "locked", _locked)

        _ext = _jdict["ext"]
        # code for union: typing.Optional[typing.Dict[str, str]]
        if json_is_type_match(typing.Dict[str, str], _ext):
            # code for arg: typing.Dict[str, str]
            _ret = _ext
            # end dict: typing.Dict[str, str]

        elif json_is_type_match(None, _ext):
            _ret = _ext
        else:
            raise ValueError(f"Unable to deserialize return value: {type(_ext)}")
        # end union: typing.Optional[typing.Dict[str, str]]

        setattr(_ret_obj, "ext", _ext)

        _ret = _ret_obj
        # end object: <class 'modelos.object.kind.ObjectInfo'>

        return _ret

    def lock(
        self, key: typing.Optional[str] = None, timeout: typing.Optional[int] = None
    ) -> None:
        """Lock the process to only operate with the caller

        Args:
            key (Optional[str], optional): An optional key to secure the lock
            timeout (Optional[int], optional): Whether to unlock after a set amount of time. Defaults to None.
        """
        # code for union: typing.Optional[str]
        if deep_isinstance(key, None):
            pass
        elif deep_isinstance(key, str):
            pass
        else:
            raise ValueError(
                "Do not know how to serialize "
                + "parameter 'key' "
                + f"of type '{type(key)}'"
            )
        # end union: typing.Optional[str]

        # code for union: typing.Optional[int]
        if deep_isinstance(timeout, None):
            pass
        elif deep_isinstance(timeout, int):
            pass
        else:
            raise ValueError(
                "Do not know how to serialize "
                + "parameter 'timeout' "
                + f"of type '{type(timeout)}'"
            )
        # end union: typing.Optional[int]

        _params = json.dumps({"key": key, "timeout": timeout}).encode("utf8")
        _headers = {"content-type": "application/json", "client-uuid": str(self.uid)}
        _req = request.Request(
            f"{self.server_addr}/lock",
            data=_params,
            headers=_headers,
        )
        _resp = request.urlopen(_req)
        _data = _resp.read().decode("utf-8")
        _jdict = json.loads(_data)

        if _jdict is None:
            raise ValueError("recieved invalid response from server, check server logs")

        if "value" in _jdict:
            _jdict = _jdict["value"]

        _ret: None
        _ret = _jdict

        return _ret

    def save(self, out_dir: str = "./artifacts") -> None:
        """Save the object

        Args:
            out_dir (str, optional): Directory to output the artiacts. Defaults to "./artifacts".
        """

        _params = json.dumps({"out_dir": out_dir}).encode("utf8")
        _headers = {"content-type": "application/json", "client-uuid": str(self.uid)}
        _req = request.Request(
            f"{self.server_addr}/save",
            data=_params,
            headers=_headers,
        )
        _resp = request.urlopen(_req)
        _data = _resp.read().decode("utf-8")
        _jdict = json.loads(_data)

        if _jdict is None:
            raise ValueError("recieved invalid response from server, check server logs")

        if "value" in _jdict:
            _jdict = _jdict["value"]

        _ret: None
        _ret = _jdict

        return _ret

    def set_d(self, name: str, ham: Ham) -> None:
        # code for object: <class '__main__.Ham'>
        ham = ham.__dict__  # type: ignore
        # end object: <class '__main__.Ham'>

        _params = json.dumps({"name": name, "ham": ham}).encode("utf8")
        _headers = {"content-type": "application/json", "client-uuid": str(self.uid)}
        _req = request.Request(
            f"{self.server_addr}/set_d",
            data=_params,
            headers=_headers,
        )
        _resp = request.urlopen(_req)
        _data = _resp.read().decode("utf-8")
        _jdict = json.loads(_data)

        if _jdict is None:
            raise ValueError("recieved invalid response from server, check server logs")

        if "value" in _jdict:
            _jdict = _jdict["value"]

        _ret: None
        _ret = _jdict

        return _ret

    def unlock(self, key: typing.Optional[str] = None, force: bool = False) -> None:
        """Unlock the kind

        Args:
            key (Optional[str], optional): Key to unlock, if needed. Defaults to None.
            force (bool, optional): Force unlock without a key. Defaults to False.
        """
        # code for union: typing.Optional[str]
        if deep_isinstance(key, None):
            pass
        elif deep_isinstance(key, str):
            pass
        else:
            raise ValueError(
                "Do not know how to serialize "
                + "parameter 'key' "
                + f"of type '{type(key)}'"
            )
        # end union: typing.Optional[str]

        _params = json.dumps({"key": key, "force": force}).encode("utf8")
        _headers = {"content-type": "application/json", "client-uuid": str(self.uid)}
        _req = request.Request(
            f"{self.server_addr}/unlock",
            data=_params,
            headers=_headers,
        )
        _resp = request.urlopen(_req)
        _data = _resp.read().decode("utf-8")
        _jdict = json.loads(_data)

        if _jdict is None:
            raise ValueError("recieved invalid response from server, check server logs")

        if "value" in _jdict:
            _jdict = _jdict["value"]

        _ret: None
        _ret = _jdict

        return _ret

    def labels(self) -> typing.Dict[str, str]:  # type: ignore
        """Labels for the resource

        Args:
            scm (Optional[SCM], optional): SCM to use. Defaults to None.

        Returns:
            Dict[str, Any]: Labels for the server
        """

        _params = json.dumps({}).encode("utf8")
        _headers = {"content-type": "application/json", "client-uuid": str(self.uid)}
        _req = request.Request(
            f"{self.server_addr}/labels",
            data=_params,
            headers=_headers,
        )
        _resp = request.urlopen(_req)
        _data = _resp.read().decode("utf-8")
        _jdict = json.loads(_data)

        if _jdict is None:
            raise ValueError("recieved invalid response from server, check server logs")

        if "value" in _jdict:
            _jdict = _jdict["value"]

        _ret: typing.Dict[str, str]
        # code for arg: typing.Dict[str, str]
        if not json_is_type_match(typing.Dict[str, str], _jdict):
            raise ValueError("JSON returned does not match type: typing.Dict[str, str]")
        _ret = _jdict
        # end dict: typing.Dict[str, str]

        return _ret

    def name(self) -> str:  # type: ignore
        """Name of the resource

        Returns:
            str: Name of the server
        """

        _params = json.dumps({}).encode("utf8")
        _headers = {"content-type": "application/json", "client-uuid": str(self.uid)}
        _req = request.Request(
            f"{self.server_addr}/name",
            data=_params,
            headers=_headers,
        )
        _resp = request.urlopen(_req)
        _data = _resp.read().decode("utf-8")
        _jdict = json.loads(_data)

        if _jdict is None:
            raise ValueError("recieved invalid response from server, check server logs")

        if "value" in _jdict:
            _jdict = _jdict["value"]

        _ret: str
        _ret = _jdict

        return _ret

    def short_name(self) -> str:  # type: ignore
        """Short name for the resource

        Returns:
            str: A short name
        """

        _params = json.dumps({}).encode("utf8")
        _headers = {"content-type": "application/json", "client-uuid": str(self.uid)}
        _req = request.Request(
            f"{self.server_addr}/short_name",
            data=_params,
            headers=_headers,
        )
        _resp = request.urlopen(_req)
        _data = _resp.read().decode("utf-8")
        _jdict = json.loads(_data)

        if _jdict is None:
            raise ValueError("recieved invalid response from server, check server logs")

        if "value" in _jdict:
            _jdict = _jdict["value"]

        _ret: str
        _ret = _jdict

        return _ret

    def _super_init(self, uri: str) -> None:
        super().__init__(uri)

    @classmethod
    def from_uri(cls: Type["DataClient"], uri: str) -> "DataClient":
        c = cls.__new__(cls)
        c._super_init(uri)
        return c
