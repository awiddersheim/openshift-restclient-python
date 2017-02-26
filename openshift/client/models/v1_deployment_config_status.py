# coding: utf-8

"""
    OpenShift API (with Kubernetes)

    OpenShift provides builds, application lifecycle, image content management, and administrative policy on top of Kubernetes. The API allows consistent management of those objects.  All API operations are authenticated via an Authorization bearer token that is provided for service accounts as a generated secret (in JWT form) or via the native OAuth endpoint located at /oauth/authorize. Core infrastructure components may use client certificates that require no authentication.  All API operations return a 'resourceVersion' string that represents the version of the object in the underlying storage. The standard LIST operation performs a snapshot read of the underlying objects, returning a resourceVersion representing a consistent version of the listed objects. The WATCH operation allows all updates to a set of objects after the provided resourceVersion to be observed by a client. By listing and beginning a watch from the returned resourceVersion, clients may observe a consistent view of the state of one or more objects. Note that WATCH always returns the update after the provided resourceVersion. Watch may be extended a limited time in the past - using etcd 2 the watch window is 1000 events (which on a large cluster may only be a few tens of seconds) so clients must explicitly handle the \"watch to old error\" by re-listing.  Objects are divided into two rough categories - those that have a lifecycle and must reflect the state of the cluster, and those that have no state. Objects with lifecycle typically have three main sections:  * 'metadata' common to all objects * a 'spec' that represents the desired state * a 'status' that represents how much of the desired state is reflected on   the cluster at the current time  Objects that have no state have 'metadata' but may lack a 'spec' or 'status' section.  Objects are divided into those that are namespace scoped (only exist inside of a namespace) and those that are cluster scoped (exist outside of a namespace). A namespace scoped resource will be deleted when the namespace is deleted and cannot be created if the namespace has not yet been created or is in the process of deletion. Cluster scoped resources are typically only accessible to admins - resources like nodes, persistent volumes, and cluster policy.  All objects have a schema that is a combination of the 'kind' and 'apiVersion' fields. This schema is additive only for any given version - no backwards incompatible changes are allowed without incrementing the apiVersion. The server will return and accept a number of standard responses that share a common schema - for instance, the common error type is 'unversioned.Status' (described below) and will be returned on any error from the API server.  The API is available in multiple serialization formats - the default is JSON (Accept: application/json and Content-Type: application/json) but clients may also use YAML (application/yaml) or the native Protobuf schema (application/vnd.kubernetes.protobuf). Note that the format of the WATCH API call is slightly different - for JSON it returns newline delimited objects while for Protobuf it returns length-delimited frames (4 bytes in network-order) that contain a 'versioned.Watch' Protobuf object.  See the OpenShift documentation at https://docs.openshift.org for more information. 

    OpenAPI spec version: v1.5.0-alpha1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1DeploymentConfigStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, available_replicas=None, conditions=None, details=None, latest_version=None, observed_generation=None, ready_replicas=None, replicas=None, unavailable_replicas=None, updated_replicas=None):
        """
        V1DeploymentConfigStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'available_replicas': 'int',
            'conditions': 'list[V1DeploymentCondition]',
            'details': 'V1DeploymentDetails',
            'latest_version': 'int',
            'observed_generation': 'int',
            'ready_replicas': 'int',
            'replicas': 'int',
            'unavailable_replicas': 'int',
            'updated_replicas': 'int'
        }

        self.attribute_map = {
            'available_replicas': 'availableReplicas',
            'conditions': 'conditions',
            'details': 'details',
            'latest_version': 'latestVersion',
            'observed_generation': 'observedGeneration',
            'ready_replicas': 'readyReplicas',
            'replicas': 'replicas',
            'unavailable_replicas': 'unavailableReplicas',
            'updated_replicas': 'updatedReplicas'
        }

        self._available_replicas = available_replicas
        self._conditions = conditions
        self._details = details
        self._latest_version = latest_version
        self._observed_generation = observed_generation
        self._ready_replicas = ready_replicas
        self._replicas = replicas
        self._unavailable_replicas = unavailable_replicas
        self._updated_replicas = updated_replicas

    @property
    def available_replicas(self):
        """
        Gets the available_replicas of this V1DeploymentConfigStatus.
        AvailableReplicas is the total number of available pods targeted by this deployment config.

        :return: The available_replicas of this V1DeploymentConfigStatus.
        :rtype: int
        """
        return self._available_replicas

    @available_replicas.setter
    def available_replicas(self, available_replicas):
        """
        Sets the available_replicas of this V1DeploymentConfigStatus.
        AvailableReplicas is the total number of available pods targeted by this deployment config.

        :param available_replicas: The available_replicas of this V1DeploymentConfigStatus.
        :type: int
        """
        if available_replicas is None:
            raise ValueError("Invalid value for `available_replicas`, must not be `None`")

        self._available_replicas = available_replicas

    @property
    def conditions(self):
        """
        Gets the conditions of this V1DeploymentConfigStatus.
        Conditions represents the latest available observations of a deployment config's current state.

        :return: The conditions of this V1DeploymentConfigStatus.
        :rtype: list[V1DeploymentCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """
        Sets the conditions of this V1DeploymentConfigStatus.
        Conditions represents the latest available observations of a deployment config's current state.

        :param conditions: The conditions of this V1DeploymentConfigStatus.
        :type: list[V1DeploymentCondition]
        """

        self._conditions = conditions

    @property
    def details(self):
        """
        Gets the details of this V1DeploymentConfigStatus.
        Details are the reasons for the update to this deployment config. This could be based on a change made by the user or caused by an automatic trigger

        :return: The details of this V1DeploymentConfigStatus.
        :rtype: V1DeploymentDetails
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this V1DeploymentConfigStatus.
        Details are the reasons for the update to this deployment config. This could be based on a change made by the user or caused by an automatic trigger

        :param details: The details of this V1DeploymentConfigStatus.
        :type: V1DeploymentDetails
        """

        self._details = details

    @property
    def latest_version(self):
        """
        Gets the latest_version of this V1DeploymentConfigStatus.
        LatestVersion is used to determine whether the current deployment associated with a deployment config is out of sync.

        :return: The latest_version of this V1DeploymentConfigStatus.
        :rtype: int
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        """
        Sets the latest_version of this V1DeploymentConfigStatus.
        LatestVersion is used to determine whether the current deployment associated with a deployment config is out of sync.

        :param latest_version: The latest_version of this V1DeploymentConfigStatus.
        :type: int
        """
        if latest_version is None:
            raise ValueError("Invalid value for `latest_version`, must not be `None`")

        self._latest_version = latest_version

    @property
    def observed_generation(self):
        """
        Gets the observed_generation of this V1DeploymentConfigStatus.
        ObservedGeneration is the most recent generation observed by the deployment config controller.

        :return: The observed_generation of this V1DeploymentConfigStatus.
        :rtype: int
        """
        return self._observed_generation

    @observed_generation.setter
    def observed_generation(self, observed_generation):
        """
        Sets the observed_generation of this V1DeploymentConfigStatus.
        ObservedGeneration is the most recent generation observed by the deployment config controller.

        :param observed_generation: The observed_generation of this V1DeploymentConfigStatus.
        :type: int
        """
        if observed_generation is None:
            raise ValueError("Invalid value for `observed_generation`, must not be `None`")

        self._observed_generation = observed_generation

    @property
    def ready_replicas(self):
        """
        Gets the ready_replicas of this V1DeploymentConfigStatus.
        Total number of ready pods targeted by this deployment.

        :return: The ready_replicas of this V1DeploymentConfigStatus.
        :rtype: int
        """
        return self._ready_replicas

    @ready_replicas.setter
    def ready_replicas(self, ready_replicas):
        """
        Sets the ready_replicas of this V1DeploymentConfigStatus.
        Total number of ready pods targeted by this deployment.

        :param ready_replicas: The ready_replicas of this V1DeploymentConfigStatus.
        :type: int
        """

        self._ready_replicas = ready_replicas

    @property
    def replicas(self):
        """
        Gets the replicas of this V1DeploymentConfigStatus.
        Replicas is the total number of pods targeted by this deployment config.

        :return: The replicas of this V1DeploymentConfigStatus.
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """
        Sets the replicas of this V1DeploymentConfigStatus.
        Replicas is the total number of pods targeted by this deployment config.

        :param replicas: The replicas of this V1DeploymentConfigStatus.
        :type: int
        """
        if replicas is None:
            raise ValueError("Invalid value for `replicas`, must not be `None`")

        self._replicas = replicas

    @property
    def unavailable_replicas(self):
        """
        Gets the unavailable_replicas of this V1DeploymentConfigStatus.
        UnavailableReplicas is the total number of unavailable pods targeted by this deployment config.

        :return: The unavailable_replicas of this V1DeploymentConfigStatus.
        :rtype: int
        """
        return self._unavailable_replicas

    @unavailable_replicas.setter
    def unavailable_replicas(self, unavailable_replicas):
        """
        Sets the unavailable_replicas of this V1DeploymentConfigStatus.
        UnavailableReplicas is the total number of unavailable pods targeted by this deployment config.

        :param unavailable_replicas: The unavailable_replicas of this V1DeploymentConfigStatus.
        :type: int
        """
        if unavailable_replicas is None:
            raise ValueError("Invalid value for `unavailable_replicas`, must not be `None`")

        self._unavailable_replicas = unavailable_replicas

    @property
    def updated_replicas(self):
        """
        Gets the updated_replicas of this V1DeploymentConfigStatus.
        UpdatedReplicas is the total number of non-terminated pods targeted by this deployment config that have the desired template spec.

        :return: The updated_replicas of this V1DeploymentConfigStatus.
        :rtype: int
        """
        return self._updated_replicas

    @updated_replicas.setter
    def updated_replicas(self, updated_replicas):
        """
        Sets the updated_replicas of this V1DeploymentConfigStatus.
        UpdatedReplicas is the total number of non-terminated pods targeted by this deployment config that have the desired template spec.

        :param updated_replicas: The updated_replicas of this V1DeploymentConfigStatus.
        :type: int
        """
        if updated_replicas is None:
            raise ValueError("Invalid value for `updated_replicas`, must not be `None`")

        self._updated_replicas = updated_replicas

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other