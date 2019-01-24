var m = require("mithril");

var CO = require("../models/CollectionObject");
var serializeForm = require("../utils/Serialize");

var clearInput = function() {
    document.getElementById("objData").reset();
},
    classe = [ "Andreoli", "ARGNANI", "BENEDETTI", "BIGARELLI", "BRAGLIA", "BUSSETTI",
    "CELLINI", "FERRARI", "FIANDRI", "GOLDONI A.", "GOLDONI C.", "JELALI",
    "MALAGOLI", "MANZONI", "MASSA", "MESCHIARI", "MESINI", "MONELLI",
    "NANNI", "PALOMBA", "PICCININI", "PUGNAGHI", "SCIPIONI", "TRALLI" ];

var Table = {
    oninit : CO.loadNext,
    view : function() {
        if (CO.curObj === {}) {
            return m("");
        } else {
            return m("form#objData.container.pure-g.pure-form",{
                onsubmit : function(e) {
                    e.preventDefault();
                    var formObj = serializeForm(document.getElementById("objData"));
                    CO.saveData(formObj.fd).then(clearInput);
                }
            }, [
                m("h4.pure-u-1-1", "Nome:"),
                m(".pure-u-1-2", CO.curObj["Nome assegnato (eventualmente provvisorio)"]),
                m(".pure-u-1-2", m("input#engName.pure-input-1[name=engName][type=text][placeholder=English name]")),
                m("h4.pure-u-1-1", "'Armadio (indicare la lettera presente a fianco della serratura)'"),
                m(".pure-u-1-1", CO.curObj["Armadio (indicare la lettera presente a fianco della serratura)"]),
                m("h4.pure-u-1-1", "Ripiano (dal basso all'alto)"),
                m(".pure-u-1-1", CO.curObj["Ripiano (dal basso all'alto)"]),
                m("h4.pure-u-1-1", "Ambito fisico"),
                m(".pure-u-1-1", CO.curObj["Ambito fisico"]),
                m("h4.pure-u-1-1", "Stato di conservazione"),
                m(".pure-u-1-1", CO.curObj["Stato di conservazione"]),
                m("h4.pure-u-1-1", "Nota sullo stato di conservazione (osservazioni, interventi suggeriti,...)"),
                m(".pure-u-1-2", CO.curObj["Nota sullo stato di conservazione (osservazioni, interventi suggeriti,...)"]),
                m(".pure-u-1-2", m("textarea#engNotes.pure-input-1[name=engNotes][placeholder=Notes]")),
                m("h4.pure-u-1-1", "Materiali (se riconoscibili)"),
                m(".pure-u-1-2", CO.curObj["Materiali (se riconoscibili)"]),
                m(".pure-u-1-2", m("input#engMaterials.pure-input-1[type=text][name=engMaterials][placeholder=Materials]")),
                m("h4.pure-u-1-1", "Breve descrizione del funzionamento (se  conosciuta)"),
                m(".pure-u-1-2", CO.curObj["Breve descrizione del funzionamento (se  conosciuta)"]),
                m(".pure-u-1-2", [
                    m("textarea#engWPrinc.pure-input-1[name=engWPrinc][placeholder=Working Principle]"),
                    m("textarea#itaWPrinc.pure-input-1[name=itaWPrinc][placeholder=Principio di funzionamento]"),
                ]),
                m("h4.pure-u-1-1", "Risorse (testi, siti web) utilizzate"),
                m(".pure-u-1-1", CO.curObj["Risorse (testi, siti web) utilizzate"]),
                m("h4.pure-u-1-1", "Gruppo di lavoro"),
                m(".pure-u-1-1", classe.map(function(alunno, i){
                    return [
                        m("input[type=checkbox]", {value : i}),
                        m("span.nome-alunno", alunno + "       ")
                    ];
                })),
                m("input#xcID[type=hidden][name=xcID]", { value : CO.curObj["ID"]}),
                m("input#salva.pure-u-1-1.pure-button.pure-button-primary.pure-button-xlarge[type=submit][value=Salva]")
            ]);
        }
    }
};

module.exports = Table;
