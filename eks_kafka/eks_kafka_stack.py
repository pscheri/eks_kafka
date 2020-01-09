from aws_cdk import (
    core,
    aws_ec2 as ec2,
    aws_eks as eks,
    aws_iam as iam,
    aws_msk as msk
)


class EksKafkaStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        vpc = ec2.Vpc(self, "EKS_Kafka_PocClusterVPC")

        private_subnets = [snet_id.subnet_id for snet_id in vpc.private_subnets]
        bngi = msk.CfnCluster.BrokerNodeGroupInfoProperty(instance_type="kafka.m5.large",
                                                          client_subnets=private_subnets)

        msk_cluster = msk.CfnCluster(self, "EKS_KafkaPocMSKCluster",
                                     broker_node_group_info=bngi,
                                     cluster_name="EKSKafkaPOCMKSCluster",
                                     kafka_version="2.3.1",
                                     number_of_broker_nodes=3)

        eks_admin_role = iam.Role(self, "EKS_Kafka_PocCluster-AdminRole",
                                  assumed_by=iam.AccountPrincipal(account_id=self.account))

        eks_cluster = eks.Cluster(self, "EKS_Kafka_PocEKSCluster",
                                  cluster_name="EKS_Kafka_PocCluster",
                                  masters_role=eks_admin_role,
                                  kubectl_enabled=True,
                                  vpc=vpc)
