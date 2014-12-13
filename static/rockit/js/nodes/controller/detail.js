define([], function () {
  'use strict';

  return ['$scope', '$routeParams', '$log', 'RockitTranslateService', 'NodeService',
    function (scope, routeParams, log, translate, service) {

      translate.addPart("nodes");

      var loadSelectedNode = function (resource) {
        if (resource) {
          service.get(resource).then(
            function (data) {
              log.debug('Successful retrieve node details', data);

              translate.addPart("nodes-" + data.association.entry);

              angular.forEach(data.commands, function (command) {
                command.partial = "/partials/commands/" + command.name;
              });

              scope.selected = data;
              scope.settings = "/partials/nodes/details/" + data.association.entry;
            },
            function () {
              log.error('Exception when trying to get node details');
            }
          );
        }
      };

      var onCreate = function () {
        var uuid = routeParams.uuid;

        log.debug('Trying to get selected node details', uuid);

        service.list().then(
          function (data) {
            var found;

            angular.forEach(data, function (node) {
              if (node.uuid === uuid) {
                found = node;
              }
            });

            if (found) {
              loadSelectedNode(found.url);
            }
          },
          function () {
            log.error('Exception when trying to get nodes', uuid);
          }
        );
      };

      onCreate();
    }];
});