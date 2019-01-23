var m = require("mithril");

var CollectionObject = require("../models/CollectionObject");


var Table = {
    oninit : CollectionObject.loadNext,
    view : function() {
        return [
            m("","ciaoo!!!!")
        ];
    }
};

module.exports = Table;
