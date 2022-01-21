from templates.schemas import generate_schemas_footer, generate_schemas_header, get_schema_string



def create_schemas(allSchemas,ext=".js"):
    for eachSchemadef in allSchemas:
        for key,schemas in eachSchemadef.items():
            name = key+ext
            with open(name,"w") as f:
                code=generate_schemas_header() 
                schema_var_name = key+"Schema"
                code += get_schema_string(schemas,schema_var_name)

                schema_model_name = f"{key}Model"
                code+=f"\n\nconst {schema_model_name} = mongoose.model('{key}',{schema_var_name})"
                code+= generate_schemas_footer(schema_model_name); 

                f.write(code)



# tokenSchema.pre("save", function (next) {
#     const currentDate = new Date();
#     this.updated = currentDate;
#     next();
# })

# const tokenModel = mongoose.model("token", tokenSchema);

# module.exports = tokenModel;     