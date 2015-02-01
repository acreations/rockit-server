define(['jquery'], function ($) {
  'use strict';

  return ['$window', function (window) {
    return {
      restrict: 'C',
      link: function (scope, element) {

        var Y_OFFSET = 0;
        var elem = $(element);

        var w = window,
          d = document,
          e = d.documentElement,
          g = d.getElementsByTagName('body')[0],
          x = w.innerWidth || e.clientWidth || g.clientWidth,
          y = w.innerHeight || e.clientHeight || g.clientHeight;

        var resize = function() {
          elem.css("min-height", ($(window).height() + Y_OFFSET));
        }

        $(window).bind('resize', function () {
          resize();
        });

        resize();
      }
    };
  }];
});