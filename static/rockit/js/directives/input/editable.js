define([], function () {
  'use strict';

  return [function () {
    return {
      restrict: 'C',
      scope: {
        model: '=ngModel',
        callback: '&onUpdate'
      },
      templateUrl: '/static/rockit/js/directives/input/editable.template',
      link: function (scope) {
        scope.cancel = function () {
          scope.editMode = false;
        };

        scope.done = function () {
          scope.editMode = false;
          scope.model = scope.edit;

          scope.callback({
            value: scope.edit
          });
        };

        scope.onEdit = function () {
          scope.editMode = true;
          scope.edit = scope.model;
        };
      }
    };
  }];
});