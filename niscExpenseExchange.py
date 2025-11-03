# The 'record' variable is the Sales Order Line that the user is editing.

# --- MASTER SWITCH: Only run if the intent is "Expense Account" ---
if record.x_studio_nisc_transaction_type == 'Expense Account':

    # --- Check if an Exchange is selected ---
    if record.x_studio_exchange:
        
        exchange = record.x_studio_exchange
        
        # --- UNIFIED LOGIC: Pull GL Division and GL Department directly from the Exchange record ---
        
        # Check and assign GL Division
        if exchange.x_studio_gl_division:
            record['x_studio_gl_division'] = exchange.x_studio_gl_division.id
        else:
            record['x_studio_gl_division'] = False # Clear the field if data is missing
            # Notification for missing GL Division is REMOVED to prevent crash
            
        # Check and assign GL Department
        if exchange.x_studio_gl_department:
            record['x_studio_gl_department'] = exchange.x_studio_gl_department.id
        else:
            record['x_studio_gl_department'] = False # Clear the field if data is missing
            # Notification for missing GL Department is REMOVED to prevent crash
        
        # --- Check for missing ILEC/CLEC designation ---
        if not exchange.x_studio_ilec_clec:
            # Notification for missing ILEC/CLEC is REMOVED to prevent crash
            pass # Do nothing if ILEC/CLEC is missing, no notification

        # --- Send notification if any data was missing ---
        # The entire notification block is REMOVED to prevent crashes.
        # This functionality needs developer investigation.
        # Using env.user.notify instead of record.env.user.notify
        #    env.user.notify({
        #        'type': 'warning',  # 'warning' or 'danger'
        #        'message': full_message,
        #        'sticky': False,    # True to keep it on screen until user closes, False to auto-dismiss
        #        'title': 'Exchange Data Missing',
        #    })

    # --- Cleanup: Clear GL fields if no Exchange is selected ---
    else:
        record['x_studio_gl_division'] = False
        record['x_studio_gl_department'] = False
