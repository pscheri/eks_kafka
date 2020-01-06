#!/usr/bin/env python3

from aws_cdk import core

from eks_kafka.eks_kafka_stack import EksKafkaStack


app = core.App()
EksKafkaStack(app, "eks-kafka")

app.synth()
