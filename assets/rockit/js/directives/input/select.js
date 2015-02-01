define(['jquery', 'selecter'], function ($) {
  'use strict';

  return ['$timeout', function (timeout) {
    return {
      restrict: 'E',
      scope: {
        model: '=ngModel',
        items: '=items'
      },
      templateUrl: '/static/rockit/js/directives/input/select.template',
      transclude: true,
      link: function (scope, element) {
        var elem = $(element);

        scope.$on('onRepeatDone', function(s, e, a) {
          elem.value = scope.model;

          timeout(function () {
            elem.selecter();
          }, 0);
        })
      }
    };
  }];
});