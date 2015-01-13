define(['jquery'], function ($) {
  'use strict';

  return [function () {
    return {
      template: '<div class="modal fade" tabindex="-1" role="dialog" aria-labelledby="modal" aria-hidden="true">' +
          '<div class="modal-dialog">' +
            '<div class="modal-content">' +
              '<div class="modal-header">' +
                '<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>' +
                '<h4 class="modal-title" data-ng-bind="title"></h4>' +
              '</div>' +
              '<div ng-transclude></div>' +
            '</div>' +
          '</div>' +
        '</div>',
      restrict: 'E',
      transclude: true,
      replace: true,
      scope: true,
      link: function postLink(scope, element, attrs) {
        scope.title = attrs.title;

        scope.$watch(attrs.visible, function (value) {
          $(element).modal(value === true ? 'show' : 'hide');
        });

        $(element).on('shown.bs.modal', function () {
          scope.$apply(function () {
            scope.$parent[attrs.visible] = true;
          });
        });

        $(element).on('hidden.bs.modal', function () {
          scope.$apply(function () {
            scope.$parent[attrs.visible] = false;
          });
        });
      }
    };
  }];
});