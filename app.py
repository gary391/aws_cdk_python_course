#!/usr/bin/env python3

from aws_cdk import core

from aws_cdk_python_course.aws_cdk_python_course_stack import AwsCdkPythonCourseStack


app = core.App()
AwsCdkPythonCourseStack(app, "aws-cdk-python-course")

app.synth()
