define(['jquery', 'bootflat'], function ($) {
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

        var elem = $(element);

        scope.$watch(attrs.visible, function (value) {
          elem.modal(value === true ? 'show' : 'hide');
        });

        elem.on('shown.bs.modal', function () {
          scope.$apply(function () {
            scope.$parent[attrs.visible] = true;
          });
        });

        elem.on('hidden.bs.modal', function () {
          scope.$apply(function () {
            scope.$parent[attrs.visible] = false;
          });
        });
      }
    };
  }];
});