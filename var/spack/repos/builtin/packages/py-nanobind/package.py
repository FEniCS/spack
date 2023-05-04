# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import os

import spack.build_systems.cmake
import spack.build_systems.python
from spack.package import *


class PyNanobind(PythonPackage):
    """nanobind -- Seamless operability between C++11 and Python.

    nanobind is a small binding library that exposes C++ types in 
    Python and vice versa. It is reminiscent of Boost.Python and pybind11 
    and uses near-identical syntax. In contrast to these existing tools,
    nanobind is more efficient: bindings compile in a shorter amount of time,
    produce smaller binaries, and have better runtime performance.
    """

    homepage = "https://nanobind.readthedocs.io"
    url = "https://github.com/wjakob/nanobind/archive/refs/tags/v1.2.0.tar.gz"
    git = "https://github.com/wjakob/nanobind.git"

    maintainers("ma595")

    version("master", branch="master", submodules=True) 
    version("1.2.0", tag="v1.2.0", submodules=True)

    depends_on("python@3.8", type=("build", "run"))
    depends_on("py-pip", type="build")
    depends_on("py-wheel", type="build")
    depends_on("py-setuptools@42:", type="build")
    depends_on("py-pytest", type="test")
    depends_on("py-scikit-build", type="run")

    depends_on("cmake@3.17:", type="run")

