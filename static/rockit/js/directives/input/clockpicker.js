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

        var lastSetValue = '';

        scope.$watch('model', function () {
          if (lastSetValue) {
            scope.model = lastSetValue;
          }
        });

        var clockpicker = $(element).clockpicker({
          'default': 'now',
          donetext: 'Done',
          afterDone: function () {
            lastSetValue = clockpicker.find("#clockpicker-value").val();
            // Set added value
            scope.$apply(function () {
              scope.model = lastSetValue;
            });
          }
        });
      }
    };
  }];
});