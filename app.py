#!/usr/bin/env python3

import os

from aws_cdk import core

from eks_kafka.eks_kafka_stack import EksKafkaStack

app = core.App()

ACCOUNT = app.node.try_get_context("account") or os.environ.get("CDK_DEFAULT_ACCOUNT", "unknown")
REGION = app.node.try_get_context("region") or os.environ.get("CDK_DEFAULT_REGION", "unknown")

ENV = core.Environment(region=REGION, account=ACCOUNT)
print("Environment is: " + str(ENV))

EksKafkaStack(app, "eks-kafka", env=ENV)

app.synth()
