/** @odoo-module */
import { ControlButtons } from "@point_of_sale/app/screens/product_screen/control_buttons/control_buttons";
import { user } from "@web/core/user";
import { patch } from "@web/core/utils/patch";
import { onWillStart } from "@odoo/owl";

patch(ControlButtons.prototype, {
    setup() {
        super.setup(...arguments);
        onWillStart(async () => {
            const currentUser = user.userId;
            
            // Definisikan semua field yang ingin diambil dalam satu array
            const fields = [
                'pos_hide_refund', 'pos_hide_info', 'pos_hide_enter_code', 
                'pos_hide_reward', 'pos_hide_reset_program', 'pos_hide_general_note', 
                'pos_hide_customer_note', 'pos_hide_pricelist', 'pos_hide_cancel_order', 
                'pos_hide_actions', 'pos_hide_quotations_order', 'pos_hide_customer', 
                'pos_hide_uploud'
            ];

            // Cukup 1 kali tembak ke server untuk mengambil semua data!
            const fetchedUsers = await this.env.services.orm.read('res.users', [currentUser], fields);
            
            if (fetchedUsers && fetchedUsers.length > 0) {
                const userData = fetchedUsers[0];
                
                // Assign nilainya secara dinamis atau satu per satu
                this.has_refund = !userData.pos_hide_refund;
                this.has_info = !userData.pos_hide_info;
                this.has_enter_code = !userData.pos_hide_enter_code;
                this.has_reward = !userData.pos_hide_reward;
                this.has_reset_program = !userData.pos_hide_reset_program;
                this.has_general_note = !userData.pos_hide_general_note;
                this.has_customer_note = !userData.pos_hide_customer_note;
                this.has_pricelist = !userData.pos_hide_pricelist;
                this.has_cancel = !userData.pos_hide_cancel_order;
                this.has_actions = !userData.pos_hide_actions;
                this.has_quotations = !userData.pos_hide_quotations_order;
                this.has_cust = !userData.pos_hide_customer;
                this.has_uploud = !userData.pos_hide_uploud;
            } else {
                // Default value jika data tidak ditemukan
                this.has_refund = this.has_info = this.has_enter_code = 
                this.has_reward = this.has_reset_program = this.has_general_note = 
                this.has_customer_note = this.has_pricelist = this.has_cancel = 
                this.has_actions = this.has_quotations = this.has_cust = 
                this.has_uploud = true;
            }
        });
    },
});