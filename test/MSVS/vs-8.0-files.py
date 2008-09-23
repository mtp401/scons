#!/usr/bin/env python
#
# __COPYRIGHT__
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

__revision__ = "__FILE__ __REVISION__ __DATE__ __DEVELOPER__"

"""
Test that we can generate Visual Studio 8.0 project (.vcproj) and
solution (.sln) files that look correct.
"""

import os
import os.path
import sys

import TestSConsMSVS

test = TestSConsMSVS.TestSConsMSVS()

# Make the test infrastructure think we have this version of MSVS installed.
test._msvs_versions = ['8.0']



expected_slnfile = """\
Microsoft Visual Studio Solution File, Format Version 9.00
# Visual Studio 2005
Project("{8BC9CEB8-8B4A-11D0-8D11-00A0C91BC942}") = "Test", "Test.vcproj", "{E5466E26-0003-F18B-8F8A-BCD76C86388D}"
EndProject
Global
\tGlobalSection(SolutionConfigurationPlatforms) = preSolution
\t\tRelease|Win32 = Release|Win32
\tEndGlobalSection
\tGlobalSection(ProjectConfigurationPlatforms) = postSolution
\t\t{E5466E26-0003-F18B-8F8A-BCD76C86388D}.Release|Win32.ActiveCfg = Release|Win32
\t\t{E5466E26-0003-F18B-8F8A-BCD76C86388D}.Release|Win32.Build.0 = Release|Win32
\tEndGlobalSection
\tGlobalSection(SolutionProperties) = preSolution
\t\tHideSolutionNode = FALSE
\tEndGlobalSection
EndGlobal
"""

expected_vcprojfile = """\
<?xml version="1.0" encoding="Windows-1252"?>
<VisualStudioProject
\tProjectType="Visual C++"
\tVersion="8.00"
\tName="Test"
\tProjectGUID="<PROJECT_GUID>"
\tSccProjectName=""
\tSccLocalPath=""
\tRootNamespace="Test"
\tKeyword="MakeFileProj">
\t<Platforms>
\t\t<Platform
\t\t\tName="Win32"/>
\t</Platforms>
\t<ToolFiles>
\t</ToolFiles>
\t<Configurations>
\t\t<Configuration
\t\t\tName="Release|Win32"
\t\t\tConfigurationType="0"
\t\t\tUseOfMFC="0"
\t\t\tATLMinimizesCRunTimeLibraryUsage="false"
\t\t\t>
\t\t\t<Tool
\t\t\t\tName="VCNMakeTool"
\t\t\t\tBuildCommandLine="echo Starting SCons &amp;&amp; &quot;<PYTHON>&quot; -c &quot;<SCONS_SCRIPT_MAIN_XML>&quot; -C &quot;<WORKPATH>&quot; -f SConstruct &quot;Test.exe&quot;"
\t\t\t\tReBuildCommandLine="echo Starting SCons &amp;&amp; &quot;<PYTHON>&quot; -c &quot;<SCONS_SCRIPT_MAIN_XML>&quot; -C &quot;<WORKPATH>&quot; -f SConstruct &quot;Test.exe&quot;"
\t\t\t\tCleanCommandLine="echo Starting SCons &amp;&amp; &quot;<PYTHON>&quot; -c &quot;<SCONS_SCRIPT_MAIN_XML>&quot; -C &quot;<WORKPATH>&quot; -f SConstruct -c &quot;Test.exe&quot;"
\t\t\t\tOutput="Test.exe"
\t\t\t\tPreprocessorDefinitions=""
\t\t\t\tIncludeSearchPath=""
\t\t\t\tForcedIncludes=""
\t\t\t\tAssemblySearchPath=""
\t\t\t\tForcedUsingAssemblies=""
\t\t\t\tCompileAsManaged=""
\t\t\t/>
\t\t</Configuration>
\t</Configurations>
\t<References>
\t</References>
\t<Files>
\t\t<Filter
\t\t\tName="Header Files"
\t\t\tFilter="h;hpp;hxx;hm;inl">
\t\t\t<File
\t\t\t\tRelativePath="sdk.h">
\t\t\t</File>
\t\t</Filter>
\t\t<Filter
\t\t\tName="Local Headers"
\t\t\tFilter="h;hpp;hxx;hm;inl">
\t\t\t<File
\t\t\t\tRelativePath="test.h">
\t\t\t</File>
\t\t</Filter>
\t\t<Filter
\t\t\tName="Other Files"
\t\t\tFilter="">
\t\t\t<File
\t\t\t\tRelativePath="readme.txt">
\t\t\t</File>
\t\t</Filter>
\t\t<Filter
\t\t\tName="Resource Files"
\t\t\tFilter="r;rc;ico;cur;bmp;dlg;rc2;rct;bin;cnt;rtf;gif;jpg;jpeg;jpe">
\t\t\t<File
\t\t\t\tRelativePath="test.rc">
\t\t\t</File>
\t\t</Filter>
\t\t<Filter
\t\t\tName="Source Files"
\t\t\tFilter="cpp;c;cxx;l;y;def;odl;idl;hpj;bat">
\t\t\t<File
\t\t\t\tRelativePath="test1.cpp">
\t\t\t</File>
\t\t\t<File
\t\t\t\tRelativePath="test2.cpp">
\t\t\t</File>
\t\t</Filter>
\t\t<File
\t\t\tRelativePath="<SCONSCRIPT>">
\t\t</File>
\t</Files>
\t<Globals>
\t</Globals>
</VisualStudioProject>
"""



SConscript_contents = """\
env=Environment(platform='win32', tools=['msvs'], MSVS_VERSION='8.0')

testsrc = ['test1.cpp', 'test2.cpp']
testincs = ['sdk.h']
testlocalincs = ['test.h']
testresources = ['test.rc']
testmisc = ['readme.txt']

env.MSVSProject(target = 'Test.vcproj',
                slnguid = '{SLNGUID}',
                srcs = testsrc,
                incs = testincs,
                localincs = testlocalincs,
                resources = testresources,
                misc = testmisc,
                buildtarget = 'Test.exe',
                variant = 'Release')
"""



test.subdir('work1')

test.write(['work1', 'SConstruct'], SConscript_contents)

test.run(chdir='work1', arguments="Test.vcproj")

test.must_exist(test.workpath('work1', 'Test.vcproj'))
vcproj = test.read(['work1', 'Test.vcproj'], 'r')
expect = test.msvs_substitute(expected_vcprojfile, '8.0', 'work1', 'SConstruct')
# don't compare the pickled data
assert vcproj[:len(expect)] == expect, test.diff_substr(expect, vcproj)

test.must_exist(test.workpath('work1', 'Test.sln'))
sln = test.read(['work1', 'Test.sln'], 'r')
expect = test.msvs_substitute(expected_slnfile, '8.0', 'work1', 'SConstruct')
# don't compare the pickled data
assert sln[:len(expect)] == expect, test.diff_substr(expect, sln)

test.run(chdir='work1', arguments='-c .')

test.must_not_exist(test.workpath('work1', 'Test.vcproj'))
test.must_not_exist(test.workpath('work1', 'Test.sln'))

test.run(chdir='work1', arguments='Test.vcproj')

test.must_exist(test.workpath('work1', 'Test.vcproj'))
test.must_exist(test.workpath('work1', 'Test.sln'))

test.run(chdir='work1', arguments='-c Test.sln')

test.must_not_exist(test.workpath('work1', 'Test.vcproj'))
test.must_not_exist(test.workpath('work1', 'Test.sln'))



# Test that running SCons with $PYTHON_ROOT in the environment
# changes the .vcproj output as expected.
os.environ['PYTHON_ROOT'] = 'xyzzy'
python = os.path.join('$(PYTHON_ROOT)', os.path.split(TestSConsMSVS.python)[1])

test.run(chdir='work1', arguments='Test.vcproj')

test.must_exist(test.workpath('work1', 'Test.vcproj'))
vcproj = test.read(['work1', 'Test.vcproj'], 'r')
expect = test.msvs_substitute(expected_vcprojfile, '8.0', 'work1', 'SConstruct',
                              python=python)
# don't compare the pickled data
assert vcproj[:len(expect)] == expect, test.diff_substr(expect, vcproj)

del os.environ['PYTHON_ROOT']
python = None



test.subdir('work2', ['work2', 'src'])

test.write(['work2', 'SConstruct'], """\
SConscript('src/SConscript', variant_dir='build')
""")

test.write(['work2', 'src', 'SConscript'], SConscript_contents)

test.run(chdir='work2', arguments=".")

vcproj = test.read(['work2', 'src', 'Test.vcproj'], 'r')
expect = test.msvs_substitute(expected_vcprojfile,
                              '8.0',
                              'work2',
                              'SConstruct',
                              project_guid="{FC63FE9E-71B3-06CC-11AF-2077D8108DFE}",
                              python=python)
# don't compare the pickled data
assert vcproj[:len(expect)] == expect, test.diff_substr(expect, vcproj)

test.must_exist(test.workpath('work2', 'src', 'Test.sln'))
sln = test.read(['work2', 'src', 'Test.sln'], 'r')
expect = test.msvs_substitute(expected_slnfile, '8.0',
                              os.path.join('work2', 'src'))
# don't compare the pickled data
assert sln[:len(expect)] == expect, test.diff_substr(expect, sln)

test.must_match(['work2', 'build', 'Test.vcproj'], """\
This is just a placeholder file.
The real project file is here:
%s
""" % test.workpath('work2', 'src', 'Test.vcproj'),
                mode='r')

test.must_match(['work2', 'build', 'Test.sln'], """\
This is just a placeholder file.
The real workspace file is here:
%s
""" % test.workpath('work2', 'src', 'Test.sln'),
                mode='r')



test.subdir('work3')

test.write(['work3', 'SConstruct'], """\
env=Environment(platform='win32', tools=['msvs'], MSVS_VERSION='8.0')

testsrc = ['test1.cpp', 'test2.cpp']
testincs = ['sdk.h']
testlocalincs = ['test.h']
testresources = ['test.rc']
testmisc = ['readme.txt']

p = env.MSVSProject(target = 'Test.vcproj',
                    srcs = testsrc,
                    incs = testincs,
                    localincs = testlocalincs,
                    resources = testresources,
                    misc = testmisc,
                    buildtarget = 'Test.exe',
                    variant = 'Release',
                    auto_build_solution = 0)

env.MSVSSolution(target = 'Test.sln',
                 slnguid = '{SLNGUID}',
                 projects = [p],
                 variant = 'Release')
""")

test.run(chdir='work3', arguments=".")

test.must_exist(test.workpath('work3', 'Test.vcproj'))
vcproj = test.read(['work3', 'Test.vcproj'], 'r')
expect = test.msvs_substitute(expected_vcprojfile, '8.0', 'work3', 'SConstruct',
                              python=python)
# don't compare the pickled data
assert vcproj[:len(expect)] == expect, test.diff_substr(expect, vcproj)

test.must_exist(test.workpath('work3', 'Test.sln'))
sln = test.read(['work3', 'Test.sln'], 'r')
expect = test.msvs_substitute(expected_slnfile, '8.0', 'work3', 'SConstruct')
# don't compare the pickled data
assert sln[:len(expect)] == expect, test.diff_substr(expect, sln)

test.run(chdir='work3', arguments='-c .')

test.must_not_exist(test.workpath('work3', 'Test.vcproj'))
test.must_not_exist(test.workpath('work3', 'Test.sln'))

test.run(chdir='work3', arguments='.')

test.must_exist(test.workpath('work3', 'Test.vcproj'))
test.must_exist(test.workpath('work3', 'Test.sln'))

test.run(chdir='work3', arguments='-c Test.sln')

test.must_exist(test.workpath('work3', 'Test.vcproj'))
test.must_not_exist(test.workpath('work3', 'Test.sln'))

test.run(chdir='work3', arguments='-c Test.vcproj')

test.must_not_exist(test.workpath('work3', 'Test.vcproj'))



test.pass_test()
