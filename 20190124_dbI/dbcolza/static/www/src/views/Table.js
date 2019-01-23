var m = require("mithril");

var CollectionObject = require("../models/CollectionObject")


var Table = {
    oninit : CollectionObject.loadNext,
    view : function() {
        return;
    }
};

module.exports = Table;
