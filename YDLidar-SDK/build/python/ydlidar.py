# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_ydlidar')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_ydlidar')
    _ydlidar = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ydlidar', [dirname(__file__)])
        except ImportError:
            import _ydlidar
            return _ydlidar
        try:
            _mod = imp.load_module('_ydlidar', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _ydlidar = swig_import_helper()
    del swig_import_helper
else:
    import _ydlidar
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _ydlidar.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _ydlidar.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _ydlidar.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _ydlidar.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _ydlidar.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _ydlidar.SwigPyIterator_equal(self, x)

    def copy(self):
        return _ydlidar.SwigPyIterator_copy(self)

    def next(self):
        return _ydlidar.SwigPyIterator_next(self)

    def __next__(self):
        return _ydlidar.SwigPyIterator___next__(self)

    def previous(self):
        return _ydlidar.SwigPyIterator_previous(self)

    def advance(self, n):
        return _ydlidar.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _ydlidar.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _ydlidar.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _ydlidar.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _ydlidar.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _ydlidar.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _ydlidar.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _ydlidar.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class PointVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PointVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PointVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _ydlidar.PointVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _ydlidar.PointVector___nonzero__(self)

    def __bool__(self):
        return _ydlidar.PointVector___bool__(self)

    def __len__(self):
        return _ydlidar.PointVector___len__(self)

    def __getslice__(self, i, j):
        return _ydlidar.PointVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _ydlidar.PointVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _ydlidar.PointVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _ydlidar.PointVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _ydlidar.PointVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _ydlidar.PointVector___setitem__(self, *args)

    def pop(self):
        return _ydlidar.PointVector_pop(self)

    def append(self, x):
        return _ydlidar.PointVector_append(self, x)

    def empty(self):
        return _ydlidar.PointVector_empty(self)

    def size(self):
        return _ydlidar.PointVector_size(self)

    def swap(self, v):
        return _ydlidar.PointVector_swap(self, v)

    def begin(self):
        return _ydlidar.PointVector_begin(self)

    def end(self):
        return _ydlidar.PointVector_end(self)

    def rbegin(self):
        return _ydlidar.PointVector_rbegin(self)

    def rend(self):
        return _ydlidar.PointVector_rend(self)

    def clear(self):
        return _ydlidar.PointVector_clear(self)

    def get_allocator(self):
        return _ydlidar.PointVector_get_allocator(self)

    def pop_back(self):
        return _ydlidar.PointVector_pop_back(self)

    def erase(self, *args):
        return _ydlidar.PointVector_erase(self, *args)

    def __init__(self, *args):
        this = _ydlidar.new_PointVector(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _ydlidar.PointVector_push_back(self, x)

    def front(self):
        return _ydlidar.PointVector_front(self)

    def back(self):
        return _ydlidar.PointVector_back(self)

    def assign(self, n, x):
        return _ydlidar.PointVector_assign(self, n, x)

    def resize(self, *args):
        return _ydlidar.PointVector_resize(self, *args)

    def insert(self, *args):
        return _ydlidar.PointVector_insert(self, *args)

    def reserve(self, n):
        return _ydlidar.PointVector_reserve(self, n)

    def capacity(self):
        return _ydlidar.PointVector_capacity(self)
    __swig_destroy__ = _ydlidar.delete_PointVector
    __del__ = lambda self: None
PointVector_swigregister = _ydlidar.PointVector_swigregister
PointVector_swigregister(PointVector)

class Str2strMap(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Str2strMap, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Str2strMap, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _ydlidar.Str2strMap_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _ydlidar.Str2strMap___nonzero__(self)

    def __bool__(self):
        return _ydlidar.Str2strMap___bool__(self)

    def __len__(self):
        return _ydlidar.Str2strMap___len__(self)
    def __iter__(self):
        return self.key_iterator()
    def iterkeys(self):
        return self.key_iterator()
    def itervalues(self):
        return self.value_iterator()
    def iteritems(self):
        return self.iterator()

    def __getitem__(self, key):
        return _ydlidar.Str2strMap___getitem__(self, key)

    def __delitem__(self, key):
        return _ydlidar.Str2strMap___delitem__(self, key)

    def has_key(self, key):
        return _ydlidar.Str2strMap_has_key(self, key)

    def keys(self):
        return _ydlidar.Str2strMap_keys(self)

    def values(self):
        return _ydlidar.Str2strMap_values(self)

    def items(self):
        return _ydlidar.Str2strMap_items(self)

    def __contains__(self, key):
        return _ydlidar.Str2strMap___contains__(self, key)

    def key_iterator(self):
        return _ydlidar.Str2strMap_key_iterator(self)

    def value_iterator(self):
        return _ydlidar.Str2strMap_value_iterator(self)

    def __setitem__(self, *args):
        return _ydlidar.Str2strMap___setitem__(self, *args)

    def asdict(self):
        return _ydlidar.Str2strMap_asdict(self)

    def __init__(self, *args):
        this = _ydlidar.new_Str2strMap(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def empty(self):
        return _ydlidar.Str2strMap_empty(self)

    def size(self):
        return _ydlidar.Str2strMap_size(self)

    def swap(self, v):
        return _ydlidar.Str2strMap_swap(self, v)

    def begin(self):
        return _ydlidar.Str2strMap_begin(self)

    def end(self):
        return _ydlidar.Str2strMap_end(self)

    def rbegin(self):
        return _ydlidar.Str2strMap_rbegin(self)

    def rend(self):
        return _ydlidar.Str2strMap_rend(self)

    def clear(self):
        return _ydlidar.Str2strMap_clear(self)

    def get_allocator(self):
        return _ydlidar.Str2strMap_get_allocator(self)

    def count(self, x):
        return _ydlidar.Str2strMap_count(self, x)

    def erase(self, *args):
        return _ydlidar.Str2strMap_erase(self, *args)

    def find(self, x):
        return _ydlidar.Str2strMap_find(self, x)

    def lower_bound(self, x):
        return _ydlidar.Str2strMap_lower_bound(self, x)

    def upper_bound(self, x):
        return _ydlidar.Str2strMap_upper_bound(self, x)
    __swig_destroy__ = _ydlidar.delete_Str2strMap
    __del__ = lambda self: None
Str2strMap_swigregister = _ydlidar.Str2strMap_swigregister
Str2strMap_swigregister(Str2strMap)

class CYdLidar(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CYdLidar, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CYdLidar, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _ydlidar.new_CYdLidar()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _ydlidar.delete_CYdLidar
    __del__ = lambda self: None

    def initialize(self):
        return _ydlidar.CYdLidar_initialize(self)

    def GetLidarVersion(self, version):
        return _ydlidar.CYdLidar_GetLidarVersion(self, version)

    def turnOn(self):
        return _ydlidar.CYdLidar_turnOn(self)

    def doProcessSimple(self, outscan):
        return _ydlidar.CYdLidar_doProcessSimple(self, outscan)

    def turnOff(self):
        return _ydlidar.CYdLidar_turnOff(self)

    def disconnecting(self):
        return _ydlidar.CYdLidar_disconnecting(self)

    def DescribeError(self):
        return _ydlidar.CYdLidar_DescribeError(self)

    def getDriverError(self):
        return _ydlidar.CYdLidar_getDriverError(self)

    def setlidaropt(self, *args):
        return _ydlidar.CYdLidar_setlidaropt(self, *args)

    def getlidaropt_toInt(self, optname):
        return _ydlidar.CYdLidar_getlidaropt_toInt(self, optname)

    def getlidaropt_toBool(self, optname):
        return _ydlidar.CYdLidar_getlidaropt_toBool(self, optname)

    def getlidaropt_toFloat(self, optname):
        return _ydlidar.CYdLidar_getlidaropt_toFloat(self, optname)

    def getlidaropt_toString(self, optname):
        return _ydlidar.CYdLidar_getlidaropt_toString(self, optname)
CYdLidar_swigregister = _ydlidar.CYdLidar_swigregister
CYdLidar_swigregister(CYdLidar)


def os_init():
    return _ydlidar.os_init()
os_init = _ydlidar.os_init

def os_isOk():
    return _ydlidar.os_isOk()
os_isOk = _ydlidar.os_isOk

def os_shutdown():
    return _ydlidar.os_shutdown()
os_shutdown = _ydlidar.os_shutdown

def lidarPortList():
    return _ydlidar.lidarPortList()
lidarPortList = _ydlidar.lidarPortList
class LaserDebug(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, LaserDebug, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, LaserDebug, name)
    __repr__ = _swig_repr
    __swig_setmethods__["W3F4CusMajor_W4F0CusMinor"] = _ydlidar.LaserDebug_W3F4CusMajor_W4F0CusMinor_set
    __swig_getmethods__["W3F4CusMajor_W4F0CusMinor"] = _ydlidar.LaserDebug_W3F4CusMajor_W4F0CusMinor_get
    if _newclass:
        W3F4CusMajor_W4F0CusMinor = _swig_property(_ydlidar.LaserDebug_W3F4CusMajor_W4F0CusMinor_get, _ydlidar.LaserDebug_W3F4CusMajor_W4F0CusMinor_set)
    __swig_setmethods__["W4F3Model_W3F0DebugInfTranVer"] = _ydlidar.LaserDebug_W4F3Model_W3F0DebugInfTranVer_set
    __swig_getmethods__["W4F3Model_W3F0DebugInfTranVer"] = _ydlidar.LaserDebug_W4F3Model_W3F0DebugInfTranVer_get
    if _newclass:
        W4F3Model_W3F0DebugInfTranVer = _swig_property(_ydlidar.LaserDebug_W4F3Model_W3F0DebugInfTranVer_get, _ydlidar.LaserDebug_W4F3Model_W3F0DebugInfTranVer_set)
    __swig_setmethods__["W3F4HardwareVer_W4F0FirewareMajor"] = _ydlidar.LaserDebug_W3F4HardwareVer_W4F0FirewareMajor_set
    __swig_getmethods__["W3F4HardwareVer_W4F0FirewareMajor"] = _ydlidar.LaserDebug_W3F4HardwareVer_W4F0FirewareMajor_get
    if _newclass:
        W3F4HardwareVer_W4F0FirewareMajor = _swig_property(_ydlidar.LaserDebug_W3F4HardwareVer_W4F0FirewareMajor_get, _ydlidar.LaserDebug_W3F4HardwareVer_W4F0FirewareMajor_set)
    __swig_setmethods__["W7F0FirewareMinor"] = _ydlidar.LaserDebug_W7F0FirewareMinor_set
    __swig_getmethods__["W7F0FirewareMinor"] = _ydlidar.LaserDebug_W7F0FirewareMinor_get
    if _newclass:
        W7F0FirewareMinor = _swig_property(_ydlidar.LaserDebug_W7F0FirewareMinor_get, _ydlidar.LaserDebug_W7F0FirewareMinor_set)
    __swig_setmethods__["W3F4BoradHardVer_W4F0Moth"] = _ydlidar.LaserDebug_W3F4BoradHardVer_W4F0Moth_set
    __swig_getmethods__["W3F4BoradHardVer_W4F0Moth"] = _ydlidar.LaserDebug_W3F4BoradHardVer_W4F0Moth_get
    if _newclass:
        W3F4BoradHardVer_W4F0Moth = _swig_property(_ydlidar.LaserDebug_W3F4BoradHardVer_W4F0Moth_get, _ydlidar.LaserDebug_W3F4BoradHardVer_W4F0Moth_set)
    __swig_setmethods__["W2F5Output2K4K5K_W5F0Date"] = _ydlidar.LaserDebug_W2F5Output2K4K5K_W5F0Date_set
    __swig_getmethods__["W2F5Output2K4K5K_W5F0Date"] = _ydlidar.LaserDebug_W2F5Output2K4K5K_W5F0Date_get
    if _newclass:
        W2F5Output2K4K5K_W5F0Date = _swig_property(_ydlidar.LaserDebug_W2F5Output2K4K5K_W5F0Date_get, _ydlidar.LaserDebug_W2F5Output2K4K5K_W5F0Date_set)
    __swig_setmethods__["W1F6GNoise_W1F5SNoise_W1F4MotorCtl_W4F0SnYear"] = _ydlidar.LaserDebug_W1F6GNoise_W1F5SNoise_W1F4MotorCtl_W4F0SnYear_set
    __swig_getmethods__["W1F6GNoise_W1F5SNoise_W1F4MotorCtl_W4F0SnYear"] = _ydlidar.LaserDebug_W1F6GNoise_W1F5SNoise_W1F4MotorCtl_W4F0SnYear_get
    if _newclass:
        W1F6GNoise_W1F5SNoise_W1F4MotorCtl_W4F0SnYear = _swig_property(_ydlidar.LaserDebug_W1F6GNoise_W1F5SNoise_W1F4MotorCtl_W4F0SnYear_get, _ydlidar.LaserDebug_W1F6GNoise_W1F5SNoise_W1F4MotorCtl_W4F0SnYear_set)
    __swig_setmethods__["W7F0SnNumH"] = _ydlidar.LaserDebug_W7F0SnNumH_set
    __swig_getmethods__["W7F0SnNumH"] = _ydlidar.LaserDebug_W7F0SnNumH_get
    if _newclass:
        W7F0SnNumH = _swig_property(_ydlidar.LaserDebug_W7F0SnNumH_get, _ydlidar.LaserDebug_W7F0SnNumH_set)
    __swig_setmethods__["W7F0SnNumL"] = _ydlidar.LaserDebug_W7F0SnNumL_set
    __swig_getmethods__["W7F0SnNumL"] = _ydlidar.LaserDebug_W7F0SnNumL_get
    if _newclass:
        W7F0SnNumL = _swig_property(_ydlidar.LaserDebug_W7F0SnNumL_get, _ydlidar.LaserDebug_W7F0SnNumL_set)
    __swig_setmethods__["W7F0Health"] = _ydlidar.LaserDebug_W7F0Health_set
    __swig_getmethods__["W7F0Health"] = _ydlidar.LaserDebug_W7F0Health_get
    if _newclass:
        W7F0Health = _swig_property(_ydlidar.LaserDebug_W7F0Health_get, _ydlidar.LaserDebug_W7F0Health_set)
    __swig_setmethods__["W3F4CusHardVer_W4F0CusSoftVer"] = _ydlidar.LaserDebug_W3F4CusHardVer_W4F0CusSoftVer_set
    __swig_getmethods__["W3F4CusHardVer_W4F0CusSoftVer"] = _ydlidar.LaserDebug_W3F4CusHardVer_W4F0CusSoftVer_get
    if _newclass:
        W3F4CusHardVer_W4F0CusSoftVer = _swig_property(_ydlidar.LaserDebug_W3F4CusHardVer_W4F0CusSoftVer_get, _ydlidar.LaserDebug_W3F4CusHardVer_W4F0CusSoftVer_set)
    __swig_setmethods__["W7F0LaserCurrent"] = _ydlidar.LaserDebug_W7F0LaserCurrent_set
    __swig_getmethods__["W7F0LaserCurrent"] = _ydlidar.LaserDebug_W7F0LaserCurrent_get
    if _newclass:
        W7F0LaserCurrent = _swig_property(_ydlidar.LaserDebug_W7F0LaserCurrent_get, _ydlidar.LaserDebug_W7F0LaserCurrent_set)
    __swig_setmethods__["MaxDebugIndex"] = _ydlidar.LaserDebug_MaxDebugIndex_set
    __swig_getmethods__["MaxDebugIndex"] = _ydlidar.LaserDebug_MaxDebugIndex_get
    if _newclass:
        MaxDebugIndex = _swig_property(_ydlidar.LaserDebug_MaxDebugIndex_get, _ydlidar.LaserDebug_MaxDebugIndex_set)

    def __init__(self):
        this = _ydlidar.new_LaserDebug()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _ydlidar.delete_LaserDebug
    __del__ = lambda self: None
LaserDebug_swigregister = _ydlidar.LaserDebug_swigregister
LaserDebug_swigregister(LaserDebug)

class LaserScan(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, LaserScan, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, LaserScan, name)
    __repr__ = _swig_repr
    __swig_setmethods__["stamp"] = _ydlidar.LaserScan_stamp_set
    __swig_getmethods__["stamp"] = _ydlidar.LaserScan_stamp_get
    if _newclass:
        stamp = _swig_property(_ydlidar.LaserScan_stamp_get, _ydlidar.LaserScan_stamp_set)
    __swig_setmethods__["points"] = _ydlidar.LaserScan_points_set
    __swig_getmethods__["points"] = _ydlidar.LaserScan_points_get
    if _newclass:
        points = _swig_property(_ydlidar.LaserScan_points_get, _ydlidar.LaserScan_points_set)
    __swig_setmethods__["config"] = _ydlidar.LaserScan_config_set
    __swig_getmethods__["config"] = _ydlidar.LaserScan_config_get
    if _newclass:
        config = _swig_property(_ydlidar.LaserScan_config_get, _ydlidar.LaserScan_config_set)

    def __init__(self):
        this = _ydlidar.new_LaserScan()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _ydlidar.delete_LaserScan
    __del__ = lambda self: None
LaserScan_swigregister = _ydlidar.LaserScan_swigregister
LaserScan_swigregister(LaserScan)

YDLIDAR_TYPE_SERIAL = _ydlidar.YDLIDAR_TYPE_SERIAL
YDLIDAR_TYPE_TCP = _ydlidar.YDLIDAR_TYPE_TCP
YDLIDAR_TYPC_UDP = _ydlidar.YDLIDAR_TYPC_UDP
TYPE_TOF = _ydlidar.TYPE_TOF
TYPE_TRIANGLE = _ydlidar.TYPE_TRIANGLE
TYPE_TOF_NET = _ydlidar.TYPE_TOF_NET
TYPE_Tail = _ydlidar.TYPE_Tail
LidarPropSerialPort = _ydlidar.LidarPropSerialPort
LidarPropIgnoreArray = _ydlidar.LidarPropIgnoreArray
LidarPropSerialBaudrate = _ydlidar.LidarPropSerialBaudrate
LidarPropLidarType = _ydlidar.LidarPropLidarType
LidarPropDeviceType = _ydlidar.LidarPropDeviceType
LidarPropSampleRate = _ydlidar.LidarPropSampleRate
LidarPropAbnormalCheckCount = _ydlidar.LidarPropAbnormalCheckCount
LidarPropMaxRange = _ydlidar.LidarPropMaxRange
LidarPropMinRange = _ydlidar.LidarPropMinRange
LidarPropMaxAngle = _ydlidar.LidarPropMaxAngle
LidarPropMinAngle = _ydlidar.LidarPropMinAngle
LidarPropScanFrequency = _ydlidar.LidarPropScanFrequency
LidarPropFixedResolution = _ydlidar.LidarPropFixedResolution
LidarPropReversion = _ydlidar.LidarPropReversion
LidarPropInverted = _ydlidar.LidarPropInverted
LidarPropAutoReconnect = _ydlidar.LidarPropAutoReconnect
LidarPropSingleChannel = _ydlidar.LidarPropSingleChannel
LidarPropIntenstiy = _ydlidar.LidarPropIntenstiy
LidarPropSupportMotorDtrCtrl = _ydlidar.LidarPropSupportMotorDtrCtrl
LidarPropSupportHeartBeat = _ydlidar.LidarPropSupportHeartBeat
class YDLidar(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, YDLidar, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, YDLidar, name)
    __repr__ = _swig_repr
    __swig_setmethods__["lidar"] = _ydlidar.YDLidar_lidar_set
    __swig_getmethods__["lidar"] = _ydlidar.YDLidar_lidar_get
    if _newclass:
        lidar = _swig_property(_ydlidar.YDLidar_lidar_get, _ydlidar.YDLidar_lidar_set)

    def __init__(self):
        this = _ydlidar.new_YDLidar()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _ydlidar.delete_YDLidar
    __del__ = lambda self: None
YDLidar_swigregister = _ydlidar.YDLidar_swigregister
YDLidar_swigregister(YDLidar)

NoError = _ydlidar.NoError
DeviceNotFoundError = _ydlidar.DeviceNotFoundError
PermissionError = _ydlidar.PermissionError
UnsupportedOperationError = _ydlidar.UnsupportedOperationError
UnknownError = _ydlidar.UnknownError
TimeoutError = _ydlidar.TimeoutError
NotOpenError = _ydlidar.NotOpenError
BlockError = _ydlidar.BlockError
NotBufferError = _ydlidar.NotBufferError
TrembleError = _ydlidar.TrembleError
LaserFailureError = _ydlidar.LaserFailureError
class LaserPoint(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, LaserPoint, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, LaserPoint, name)
    __repr__ = _swig_repr
    __swig_setmethods__["angle"] = _ydlidar.LaserPoint_angle_set
    __swig_getmethods__["angle"] = _ydlidar.LaserPoint_angle_get
    if _newclass:
        angle = _swig_property(_ydlidar.LaserPoint_angle_get, _ydlidar.LaserPoint_angle_set)
    __swig_setmethods__["range"] = _ydlidar.LaserPoint_range_set
    __swig_getmethods__["range"] = _ydlidar.LaserPoint_range_get
    if _newclass:
        range = _swig_property(_ydlidar.LaserPoint_range_get, _ydlidar.LaserPoint_range_set)
    __swig_setmethods__["intensity"] = _ydlidar.LaserPoint_intensity_set
    __swig_getmethods__["intensity"] = _ydlidar.LaserPoint_intensity_get
    if _newclass:
        intensity = _swig_property(_ydlidar.LaserPoint_intensity_get, _ydlidar.LaserPoint_intensity_set)

    def __init__(self):
        this = _ydlidar.new_LaserPoint()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _ydlidar.delete_LaserPoint
    __del__ = lambda self: None
LaserPoint_swigregister = _ydlidar.LaserPoint_swigregister
LaserPoint_swigregister(LaserPoint)

class LaserConfig(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, LaserConfig, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, LaserConfig, name)
    __repr__ = _swig_repr
    __swig_setmethods__["min_angle"] = _ydlidar.LaserConfig_min_angle_set
    __swig_getmethods__["min_angle"] = _ydlidar.LaserConfig_min_angle_get
    if _newclass:
        min_angle = _swig_property(_ydlidar.LaserConfig_min_angle_get, _ydlidar.LaserConfig_min_angle_set)
    __swig_setmethods__["max_angle"] = _ydlidar.LaserConfig_max_angle_set
    __swig_getmethods__["max_angle"] = _ydlidar.LaserConfig_max_angle_get
    if _newclass:
        max_angle = _swig_property(_ydlidar.LaserConfig_max_angle_get, _ydlidar.LaserConfig_max_angle_set)
    __swig_setmethods__["angle_increment"] = _ydlidar.LaserConfig_angle_increment_set
    __swig_getmethods__["angle_increment"] = _ydlidar.LaserConfig_angle_increment_get
    if _newclass:
        angle_increment = _swig_property(_ydlidar.LaserConfig_angle_increment_get, _ydlidar.LaserConfig_angle_increment_set)
    __swig_setmethods__["time_increment"] = _ydlidar.LaserConfig_time_increment_set
    __swig_getmethods__["time_increment"] = _ydlidar.LaserConfig_time_increment_get
    if _newclass:
        time_increment = _swig_property(_ydlidar.LaserConfig_time_increment_get, _ydlidar.LaserConfig_time_increment_set)
    __swig_setmethods__["scan_time"] = _ydlidar.LaserConfig_scan_time_set
    __swig_getmethods__["scan_time"] = _ydlidar.LaserConfig_scan_time_get
    if _newclass:
        scan_time = _swig_property(_ydlidar.LaserConfig_scan_time_get, _ydlidar.LaserConfig_scan_time_set)
    __swig_setmethods__["min_range"] = _ydlidar.LaserConfig_min_range_set
    __swig_getmethods__["min_range"] = _ydlidar.LaserConfig_min_range_get
    if _newclass:
        min_range = _swig_property(_ydlidar.LaserConfig_min_range_get, _ydlidar.LaserConfig_min_range_set)
    __swig_setmethods__["max_range"] = _ydlidar.LaserConfig_max_range_set
    __swig_getmethods__["max_range"] = _ydlidar.LaserConfig_max_range_get
    if _newclass:
        max_range = _swig_property(_ydlidar.LaserConfig_max_range_get, _ydlidar.LaserConfig_max_range_set)

    def __init__(self):
        this = _ydlidar.new_LaserConfig()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _ydlidar.delete_LaserConfig
    __del__ = lambda self: None
LaserConfig_swigregister = _ydlidar.LaserConfig_swigregister
LaserConfig_swigregister(LaserConfig)

class LaserFan(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, LaserFan, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, LaserFan, name)
    __repr__ = _swig_repr
    __swig_setmethods__["stamp"] = _ydlidar.LaserFan_stamp_set
    __swig_getmethods__["stamp"] = _ydlidar.LaserFan_stamp_get
    if _newclass:
        stamp = _swig_property(_ydlidar.LaserFan_stamp_get, _ydlidar.LaserFan_stamp_set)
    __swig_setmethods__["npoints"] = _ydlidar.LaserFan_npoints_set
    __swig_getmethods__["npoints"] = _ydlidar.LaserFan_npoints_get
    if _newclass:
        npoints = _swig_property(_ydlidar.LaserFan_npoints_get, _ydlidar.LaserFan_npoints_set)
    __swig_setmethods__["points"] = _ydlidar.LaserFan_points_set
    __swig_getmethods__["points"] = _ydlidar.LaserFan_points_get
    if _newclass:
        points = _swig_property(_ydlidar.LaserFan_points_get, _ydlidar.LaserFan_points_set)
    __swig_setmethods__["config"] = _ydlidar.LaserFan_config_set
    __swig_getmethods__["config"] = _ydlidar.LaserFan_config_get
    if _newclass:
        config = _swig_property(_ydlidar.LaserFan_config_get, _ydlidar.LaserFan_config_set)

    def __init__(self):
        this = _ydlidar.new_LaserFan()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _ydlidar.delete_LaserFan
    __del__ = lambda self: None
LaserFan_swigregister = _ydlidar.LaserFan_swigregister
LaserFan_swigregister(LaserFan)

class string_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, string_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, string_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["data"] = _ydlidar.string_t_data_set
    __swig_getmethods__["data"] = _ydlidar.string_t_data_get
    if _newclass:
        data = _swig_property(_ydlidar.string_t_data_get, _ydlidar.string_t_data_set)

    def __init__(self):
        this = _ydlidar.new_string_t()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _ydlidar.delete_string_t
    __del__ = lambda self: None
string_t_swigregister = _ydlidar.string_t_swigregister
string_t_swigregister(string_t)

class LidarPort(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, LidarPort, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, LidarPort, name)
    __repr__ = _swig_repr
    __swig_setmethods__["port"] = _ydlidar.LidarPort_port_set
    __swig_getmethods__["port"] = _ydlidar.LidarPort_port_get
    if _newclass:
        port = _swig_property(_ydlidar.LidarPort_port_get, _ydlidar.LidarPort_port_set)

    def __init__(self):
        this = _ydlidar.new_LidarPort()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _ydlidar.delete_LidarPort
    __del__ = lambda self: None
LidarPort_swigregister = _ydlidar.LidarPort_swigregister
LidarPort_swigregister(LidarPort)

class LidarVersion(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, LidarVersion, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, LidarVersion, name)
    __repr__ = _swig_repr
    __swig_setmethods__["hardware"] = _ydlidar.LidarVersion_hardware_set
    __swig_getmethods__["hardware"] = _ydlidar.LidarVersion_hardware_get
    if _newclass:
        hardware = _swig_property(_ydlidar.LidarVersion_hardware_get, _ydlidar.LidarVersion_hardware_set)
    __swig_setmethods__["soft_major"] = _ydlidar.LidarVersion_soft_major_set
    __swig_getmethods__["soft_major"] = _ydlidar.LidarVersion_soft_major_get
    if _newclass:
        soft_major = _swig_property(_ydlidar.LidarVersion_soft_major_get, _ydlidar.LidarVersion_soft_major_set)
    __swig_setmethods__["soft_minor"] = _ydlidar.LidarVersion_soft_minor_set
    __swig_getmethods__["soft_minor"] = _ydlidar.LidarVersion_soft_minor_get
    if _newclass:
        soft_minor = _swig_property(_ydlidar.LidarVersion_soft_minor_get, _ydlidar.LidarVersion_soft_minor_set)
    __swig_setmethods__["soft_patch"] = _ydlidar.LidarVersion_soft_patch_set
    __swig_getmethods__["soft_patch"] = _ydlidar.LidarVersion_soft_patch_get
    if _newclass:
        soft_patch = _swig_property(_ydlidar.LidarVersion_soft_patch_get, _ydlidar.LidarVersion_soft_patch_set)
    __swig_setmethods__["sn"] = _ydlidar.LidarVersion_sn_set
    __swig_getmethods__["sn"] = _ydlidar.LidarVersion_sn_get
    if _newclass:
        sn = _swig_property(_ydlidar.LidarVersion_sn_get, _ydlidar.LidarVersion_sn_set)

    def __init__(self):
        this = _ydlidar.new_LidarVersion()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _ydlidar.delete_LidarVersion
    __del__ = lambda self: None
LidarVersion_swigregister = _ydlidar.LidarVersion_swigregister
LidarVersion_swigregister(LidarVersion)


def LaserFanInit(to_init):
    return _ydlidar.LaserFanInit(to_init)
LaserFanInit = _ydlidar.LaserFanInit

def LaserFanDestroy(to_destroy):
    return _ydlidar.LaserFanDestroy(to_destroy)
LaserFanDestroy = _ydlidar.LaserFanDestroy
# This file is compatible with both classic and new-style classes.


