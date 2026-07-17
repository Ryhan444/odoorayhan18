/** @odoo-module */
import { user } from "@web/core/user";
import { patch } from "@web/core/utils/patch";
import { onWillStart } from "@odoo/owl";
import {
    NoteButton,
    InternalNoteButton,
} from "@point_of_sale/app/screens/product_screen/control_buttons/orderline_note_button/orderline_note_button";
patch(NoteButton.prototype, {
    setup() {
        super.setup(...arguments);
        onWillStart(async () => {
            const currentUser = user.userId;
            const fetchedUser = await this.env.services.orm.read('res.users', [currentUser], ['pos_hide_general_note']);
            if (fetchedUser && fetchedUser.length > 0) {
                    this.pos_hide_general_note = fetchedUser[0].pos_hide_general_note;
                    this.has_general_note = !this.pos_hide_general_note; // true jika pos_hide_general_note false
            } else {
                    this.has_general_note = true; // Set default value
            }
        });
    },

})

