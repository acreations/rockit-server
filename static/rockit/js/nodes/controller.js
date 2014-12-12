define(['angular', 'nodes/service'], function (angular) {
  'use strict';

  return angular.module('rockit.nodes', ['rockit.nodes.service'])

    .controller('NodesCtrl', ['$scope', '$log', 'NodesService', function (scope, log, service) {

      scope.loadNode = function (resource) {
        log.debug('Trying to load node', resource);

        service.get(resource).then(
          function (data) {
            log.debug('Successful get node', data);

            scope.selected = data;
          },
          function () {
            log.error('Exception when trying to get node');
          }
        );
      };

      scope.loadNodes = function () {
        log.debug('Load rockit settings');

        service.list().then(
          function (data) {
            log.debug('Successful got nodes', data);

            scope.nodes = data;
          },
          function () {
            log.error('Exception when trying to load services');
          }
        );
      };

      scope.updateName = function (node, name) {
        if (node.name !== name) {
          log.debug('Trying to update name of node', node, name);

          var update = {
            'name': name,
            'association': node.association,
          };

          service.update(node.url, update).then(
            function (data) {
              log.debug('Successful updated name', data);
            },
            function () {
              log.error('Exception when trying to update name');
            }
          );

        } else {
          log.debug('Trying to change to same name ... skipping');
        }
      };
    }]);
});