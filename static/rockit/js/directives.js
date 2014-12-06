define(['angular'], function (angular) {
  'use strict';

  return angular.module('rockit.directives', [])
    .directive('editable', [function () {
      return {
        restricted: 'E',
        scope: {
          model: '=ngModel',
          callback: '&onUpdate'
        },
        template: '<span data-ng-bind="model" data-ng-click="onEdit()" data-ng-hide="editMode"></span>' +
          '<input data-ng-model="edit" data-ng-show="editMode" data-ng-blur="done()"></input>' +
          '<p class="clearfix" data-ng-show="editMode">' +
            '<button type="button" class="btn btn-success btn-xs" data-ng-click="done()">Save</button>' +
            '<button type="button" class="btn btn-xs" data-ng-click="cancel()">Cancel</button>' +
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
    }]);
});