define(['angular', 'associations/service'], function (angular) {
  'use strict';

  return angular.module('rockit.associations', ['rockit.associations.service'])
    .controller('AssociationsCtrl', ['$scope', '$log', 'AssociationsService', function (scope, log, service) {

      /*
       * Get all associations
       */
      scope.loadAssociations =  function () {
        service.list().then(
          function (data) {
            log.debug('Successful retrieved associations', data);

            scope.associations = data;
          },
          function () {
            log.error('Exception when trying to get associations');
          }
        );
      };
    }]);
});