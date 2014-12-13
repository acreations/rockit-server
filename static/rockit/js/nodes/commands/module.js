/**
 * Module for handle nodes
 */
define(['angular',
  './directives/switch-binary'], function (ng, switchbinary) {
  'use strict';

  var module = ng.module("rockit.nodes.commands", []);

  return module
    .directive('switchbinary', switchbinary);
});