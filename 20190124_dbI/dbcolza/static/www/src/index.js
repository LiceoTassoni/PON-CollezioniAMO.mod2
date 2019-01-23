var m = require("mithril");
var Table = require("./views/Table");

var root = document.body;

m.route(root, "/", {
    "/" : {
        render : function() {
            return m(Table);
        }
    },
});
