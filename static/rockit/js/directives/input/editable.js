define([], function () {
  'use strict';

  return [function () {
    return {
      restrict: 'C',
      scope: {
        model: '=ngModel',
        callback: '&onUpdate'
      },
      template: '<h4 data-ng-bind="model" data-ng-click="onEdit()" data-ng-hide="editMode"></h4>' +
        '<form class="form-inline" role="form">' +
          '<div class="form-group">' +
            '<input class="form-control" data-ng-model="edit" data-ng-blur="done()"></input>' +
            '<button type="button" class="btn btn-primary" data-ng-click="done()">Save</button>' +
            '<button type="button" class="btn" data-ng-click="cancel()">Cancel</button>' +
          '</div>' +
        '</form>',
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