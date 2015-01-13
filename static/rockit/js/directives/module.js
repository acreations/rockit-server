/**
 * Module for handle nodes
 */
define(['angular',
  './callback/repeat',
  './input/editable',
  './input/select',
  './navigation/breadcrumb',
  './navigation/navbar',
  './window/filler',
  './window/modal'], function (ng, repeatDone, editable, select, breadcrumb, navbar, filler, modal) {
  'use strict';

  var module = ng.module("rockit.directives", []);

  return module
    .directive('breadcrumb', breadcrumb)
    .directive('editable', editable)
    .directive('navbar', navbar)
    .directive('filler', filler)
    .directive('callbackOnRepeatDone', repeatDone)
    .directive('modal', modal)
    .directive('select', select);
});