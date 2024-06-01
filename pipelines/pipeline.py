import kfp
from kfp import dsl
from kfp.components import create_component_from_func

# Define a component for data preprocessing
def preprocess():
    return dsl.ContainerOp(
        name='Preprocess Data',
        image='your-registry/data-preprocess:latest',
        command=['python', 'src/data/preprocess.py']
    )

# Define a component for model training
def train():
    return dsl.ContainerOp(
        name='Train Model',
        image='your-registry/model-train:latest',
        command=['python', 'src/models/train.py']
    )

# Define the pipeline
@dsl.pipeline(
   name='Iris Training Pipeline',
   description='An example pipeline that trains an Iris model.'
)
def iris_pipeline():
    preprocess_task = preprocess()
    train_task = train()
    train_task.after(preprocess_task)

# Compile the pipeline
if __name__ == '__main__':
    kfp.compiler.Compiler().compile(iris_pipeline, 'iris_pipeline.yaml')
