odoo.gestao_compras = function (instance){
    var QWeb = openerp.web.qweb;
    _t = instance.web._t;
    var self = this;
odoo.web.ListView.include({
    load_list: function(data) {
        this._super(data);
        if (this.$buttons) {
            this.$buttons.find('.oe_new_button').off().click(this.proxy('do_the_job')) ;
            console.log('AAA & Close button method call...');
        }
    },
    do_the_job: function () {
        this.do_action({
            type: "ir.actions.act_window",
            name: "Создание нового проекта",
            res_model: "despesa.despesa",
            views: [[false,'form']],
            target: 'current',
            view_type : 'form',
            view_mode : 'form',
            flags: {'form': {'action_buttons': true, 'options': {'mode': 'edit'}}}
        });
        return {
                'type': 'ir.actions.client',
                'tag': 'reload',
        }
}
});
}