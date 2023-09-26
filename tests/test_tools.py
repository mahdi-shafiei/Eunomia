#!/usr/bin/env python

"""Tests for `eunomia` package."""

import unittest

import eunomia


class TestGeneral(unittest.TestCase):
    def test_tools(self):
        tool_names = list(eunomia.EunomiaTools.all_tools_dict.keys())
        vectorstore = "test_files/test_vector_store.pkl"
        return eunomia.EunomiaTools(
            tool_names=tool_names, vectorstore=vectorstore
        ).get_tools()

    def test_initialize_agent(self):
        tool_names = list(eunomia.EunomiaTools.all_tools_dict.keys())
        vectorstore = "test_files/test_vector_store.pkl"
        tools = eunomia.EunomiaTools(
            tool_names=tool_names, vectorstore=vectorstore
        ).get_tools()
        return eunomia.Eunomia(tools=tools, model="gpt-4", get_cost=True)


if __name__ == "__main__":
    unittest.main()
