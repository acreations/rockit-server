define([], function () {
  'use strict';

  return ['$scope', '$location', '$log', 'NodeService', function (scope, location, log, service) {

    scope.getAvailableNodes = function () {
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

    scope.onSelectedNode = function(node) {
      if (node) {
        location.path('/nodes/' + node.uuid);
      } else {
        log.error('No node is selected');
      }
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

    scope.getAvailableNodes();
  }];
});