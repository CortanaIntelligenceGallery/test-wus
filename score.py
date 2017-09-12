# This script generates the scoring and schema files
# necessary to operationalize your model
from azure.ml.api.schema.dataTypes import DataTypes
from azure.ml.api.schema.sampleDefinition import SampleDefinition
from azure.ml.api.realtime.services import generate_schema
from azureml.assets import get_local_path

# Prepare the web service definition by authoring
# init() and run() functions. Test the functions
# before deploying the web service.
def init():
    # Get the path to the model asset
    # local_path = get_local_path('./assets/mymodel.model.link')
    
    # Load model using appropriate library and function
    global model
    # model = model_load_function(local_path)

def run(input_df):
    import json
    
    # Predict using appropriate functions
    # pred = model.predict(input_df)

    return json.dumps(str(pred[0]))

# Implement test code to run in IDE or Azure ML Workbench
if __name__ == '__main__':
    init()
    input = "{}"
    run(input)
