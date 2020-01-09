from aws_cdk import (
    core,
    aws_eks as eks,
    aws_iam as iam
)


class EksKafkaStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # vpc = ec2.Vpc(self, "EKS_Kafka_PocClusterVPC", is_default=True)

        eks_admin_role = iam.Role(self, "EKS_Kafka_PocCluster-AdminRole",
                                  assumed_by=iam.AccountPrincipal(account_id=self.account))

        cluster = eks.Cluster(self, "EKS_Kafka_PocCluster",
                              cluster_name="EKS_Kafka_PocCluster",
                              masters_role=eks_admin_role,
                              kubectl_enabled=True)
