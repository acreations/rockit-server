/**
 * Module for handle nodes
 */
define(['angular',
  './input/editable',
  './navigation/breadcrumb',
  './navigation/navbar',
  './window/filler'], function (ng, editable, breadcrumb, navbar, filler) {
  'use strict';

  var module = ng.module("rockit.directives", []);

  return module
    .directive('breadcrumb', breadcrumb)
    .directive('editable', editable)
    .directive('navbar', navbar)
    .directive('filler', filler);
});