define([], function () {
  'use strict';

  return [function () {
    return {
      restrict: 'E',
      scope: {
        model: '=ngModel',
        callback: '&onUpdate'
      },
      template: '<h4 data-ng-bind="model" data-ng-click="onEdit()" data-ng-hide="editMode"></h4>' +
        '<input class="input-lg" data-ng-model="edit" data-ng-show="editMode" data-ng-blur="done()"></input>' +
        '<div data-ng-show="editMode">' +
          '<button type="button" class="btn btn-primary btn-sm" data-ng-click="done()">Save</button>' +
          '<button type="button" class="btn btn-sm" data-ng-click="cancel()">Cancel</button>' +
        '</p>',
      translude: true,
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