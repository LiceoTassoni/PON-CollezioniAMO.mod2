var m = require("mithril");

var root = document.body;

m.route(root, "/", {
    "/" : {
        render : function() {
            return m("a.pure-button.pure-button-primary.pure-button-xlarge#startbtn",
                {
                    href : "/edit", oncreate: m.route.link
                },
                "INIZIA!"
            );
        }
    },
});
