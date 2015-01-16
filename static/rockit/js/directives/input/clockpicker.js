define(['jquery', 'clockpicker'], function ($) {
  'use strict';

  return [function () {
    return {
      restrict: 'C',
      scope: {
        model: '=ngModel'
      },
      templateUrl: '/static/rockit/js/directives/input/clockpicker.template',
      link: function (scope, element) {

        var clockpicker = $(element).clockpicker({
          'default': 'now',
          donetext: 'Set',
          afterDone: function () {
            // Set added value
            scope.$apply(function () {
              scope.model = clockpicker.find("#clockpicker-value").val();
            });
          }
        });
      }
    };
  }];
});