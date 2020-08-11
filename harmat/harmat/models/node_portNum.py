"""
Node class
Author: hki34
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

#from builtins import dict

from future import standard_library

import warnings

#standard_library.install_aliases()


class Node_PN(object):
    """
    This class defines a Node object which describes any type of node which is used
    in HARM. It may be a host, vulnerability or anything else. It is used in any
    type of any graph model such as: Attack Graph, Attack Tree and HARM.
    """

    def __init__(self):
        # super(Node, self).__setattr__('values', dict())
        self.__dict__['values'] = dict()

    def __getattr__(self, item):
        if 'values' not in self.__dict__:  # Fix issues with deepcopy
            self.__dict__['values'] = dict()
        if item in self.__dict__['values']:
            return self.__dict__['values'][item]
        return self.__getattribute__(item)

    def __setattr__(self, key, value):
        if key in ['name', 'threat_class', 'gatetype', 'middle_layer']:
            self.__dict__[key] = value
        elif key == 'values':
            self.values.update(value)
        elif key == 'meta':
            self.meta.update(value)
        else:
            self.values[key] = value



class LogicGate(Node_PN):
    VALID_GATES = ['or', 'and']
    def __init__(self, gatetype):
        Node_PN.__init__(self)
        self.gatetype = gatetype

    def validate_gatetype(self, gt):
        """
        Check that the gatetype string is a valid one

        Args:
            gt: The string to input check
        Returns:
            Boolean.
        """
        if gt not in self.VALID_GATES:
            return False
        return True

    def __repr__(self):
        return '{}:{}'.format(self.__class__.__name__, self.gatetype)


class Host_PN(Node_PN):
    def __init__(self, name, values=None):
        Node_PN.__init__(self)
        self.__dict__['meta'] = dict()
        self.__dict__['_values'] = dict()
        self.name = name
        self.middle_layer = None
        self.ignorable = False
        if values is not None:
            self.__dict__['_values'].update(values)

    def __getattr__(self, item):
        if item in ['__deepcopy__', '__setstate__', '__getstate__']:
            return self.__getattribute__(item)
        if 'values' not in self.__dict__:  # Fix issues with deepcopy
            self.__dict__['_values'] = dict()
        if item in self.__dict__['_values']:
            self.update_value_dict()
            return self.__dict__['_values'][item]
        elif self.__dict__['middle_layer'] is not None and item in self.__dict__['middle_layer'].rootnode.values:
            return self.__dict__['middle_layer'].rootnode.values[item]
        return self.__getattribute__(item)


    def __setattr__(self, key, value):
        if key in ['name', 'gatetype', 'middle_layer', 'ignorable']:
            self.__dict__[key] = value
        elif key == 'values':
            self.__dict__['_values'].update(value)
        elif key == 'meta':
            self.meta.update(value)
        else:
            self.values[key] = value

    @property
    def values(self):
        v = self.__dict__['_values']
        if self.middle_layer is not None:
            v.update(self.middle_layer.rootnode.values)
        return v

    def flowup(self):
        self.middle_layer.flowup()

    def update_value_dict(self):
        if self.middle_layer is not None:
            self.__dict__['values'].update(self.middle_layer.rootnode.values)

    def __repr__(self):
        return '{}:{}'.format(self.__class__.__name__, self.name)



'''not tested - Testing the port number'''
class PortNumber(Node_PN):
    def __init__(self, name,  values=None):
        Node_PN.__init__(self)
        self.name = name
        if values is not None:
            self.values.update(values)

    def __repr__(self):
        return '{}:{}'.format(self.__class__.__name__, self.name)