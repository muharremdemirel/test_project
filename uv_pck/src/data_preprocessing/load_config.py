from pydantic import BaseModel, Field
from typing import List, Optional

class PreprocessorConfig(BaseModel):
    pass
class FeatureConfig(BaseModel):
    numerical: List[str] = Field(default_factory=list, description="List of numerical features.")
    categorical: List[str] = Field(default_factory=list, description="List of categorical features.")

class StepsConfig(BaseModel):
    preprocessor: PreprocessorConfig = Field(default_factory=PreprocessorConfig, description="Configuration for the preprocessor.")
    features: FeatureConfig = Field(default_factory=FeatureConfig, description="Configuration for the features.")