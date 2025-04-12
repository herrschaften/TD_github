# me - this DAT
# scriptOp - the OP which is cooking
# press 'Setup Parameters' in the OP to call this function to re-create the parameters.
def onSetupParameters(scriptOp):
    page = scriptOp.appendCustomPage('Custom')
    p = page.appendFloat('Newwidth', label='New Width')
    # Set the expression directly in the parameter
    p = (op('fit2').height/op('moviefilein1').height)*op('moviefilein1').width
    return

# called whenever custom pulse parameter is pushed
def onPulse(par):
    return

def onCook(scriptOp):
    scriptOp.clear()
    # Access the parameter value
    new_width = scriptOp.par.Newwidth.eval()
    # Create a channel with the parameter value
    scriptOp.appendChan('newWidth')
    scriptOp[0] = new_width
    return