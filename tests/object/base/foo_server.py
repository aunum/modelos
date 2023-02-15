# This file was generated by ModelOS
import json
import logging
import os

# from base_test import *  # noqa
# from base_test import Foo
import typing
from typing import List

import base_test
import uvicorn
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import BaseRoute, Route

from modelos.object.encoding import deep_isinstance

log_level = os.getenv("LOG_LEVEL")
if log_level is None:
    logging.basicConfig(level=logging.INFO)
else:
    logging.basicConfig(level=log_level)


class FooServer(base_test.Foo):
    """A resource server for Foo"""

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

    async def _test_req(self, request):
        """Request for function:
        test(self) -> None
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
        _ret = self.test(**_jdict)
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
            Route("/health", endpoint=self._health_req, methods=["GET", "POST"]),
            Route("/info", endpoint=self._info_req, methods=["POST"]),
            Route("/lock", endpoint=self._lock_req, methods=["POST"]),
            Route("/save", endpoint=self._save_req, methods=["POST"]),
            Route("/test", endpoint=self._test_req, methods=["POST"]),
            Route("/unlock", endpoint=self._unlock_req, methods=["POST"]),
            Route("/labels", endpoint=self._labels_req, methods=["POST"]),
            Route("/name", endpoint=self._name_req, methods=["POST"]),
            Route("/short_name", endpoint=self._short_name_req, methods=["POST"]),
        ]


o = FooServer.from_env()
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