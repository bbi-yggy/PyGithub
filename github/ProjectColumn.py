# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2018 bbi-yggy <yossarian@blackbirdinteractive.com>                 #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.readthedocs.io/                                              #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
################################################################################

import json

import github.GithubObject
import github.Project
import github.ProjectCard

# TODO: remaining ProjectColumn properties
class ProjectColumn(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents Project Columns. The reference can be found here http://developer.github.com/v3/projects/columns
    """

    def __repr__(self):
        return self.get__repr__({"name": self._name.value})

    @property
    def id(self):
        """
        :type: integer
        """
        return self._id.value

    @property
    def name(self):
        """
        :type: string
        """
        return self._name.value

    @property
    def url(self):
        """
        :type: string
        """
        return self._url.value

    def get_cards(self,archived_state=github.GithubObject.NotSet):
        """
        :calls: `GET /projects/columns/:column_id/cards <https://developer.github.com/v3/projects/cards/#list-project-cards>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.ProjectCard.ProjectCard`
        :param archived_state: string
        """
        assert archived_state is github.GithubObject.NotSet or isinstance(archived_state, (str, unicode)), archived_state

        url_parameters = dict()
        if archived_state is not github.GithubObject.NotSet:
            url_parameters["archived_state"] = archived_state

        return github.PaginatedList.PaginatedList(
            github.ProjectCard.ProjectCard,
            self._requester,
            self.url + "/cards",
            url_parameters,
            github.Project.PROJECT_PREVIEW_HEADERS
        )

    def _initAttributes(self):
        self._id = github.GithubObject.NotSet
        self._name = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "url" in attributes:  # pragma no branch
            assert attributes["url"] is None or isinstance(attributes["url"], (str, unicode)), attributes["url"]
            self._url = self._makeStringAttribute(attributes["url"])

