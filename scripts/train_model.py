#Importación de métricas
from sklearn.model_selection import cross_val_score, GridSearchCV

#Importación de modelos de clasificación
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR

#Creamos listas para almacenar los resultados obtenidos de los distintos modelos
  #modelos
models = ['Linear Regression', 'Ridge', 'Lasso', 'KNN', 'Decision Tree','Random Forest', 'Gradient Boosting', 'SVR']

  #métricas
MAE_scores = []
MSE_scores = []
RMSE_scores = []
R2_scores = []

#Definición de los modelos
linear_model = LinearRegression()
ridge_model = Ridge()
lasso_model = Lasso()
knn_model = KNeighborsRegressor()
tree_model = DecisionTreeRegressor()
rf_model = RandomForestRegressor()
gb_model = GradientBoostingRegressor()
svr_model = SVR()

#Lista de modelos
model_list = [linear_model, ridge_model, lasso_model, knn_model, tree_model, rf_model, gb_model, svr_model]

#Entrenamiento y evaluacion de cada modelo
predictions = {}

for name, model in zip(models, model_list):
  model.fit(X_train, y_train)
  y_pred = model.predict(X_test)
  predictions[name] = y_pred

  MAE_scores.append(mean_absolute_error(y_test, y_pred))
  MSE_scores.append(mean_squared_error(y_test, y_pred))
  RMSE_scores.append(root_mean_squared_error(y_test, y_pred))
  R2_scores.append(r2_score(y_test, y_pred))


#Creación de dataframe para los resultados
results_df_orig = pd.DataFrame({
    'Model': models,
    'MAE': MAE_scores,
    'MSE': MSE_scores,
    'RMSE': RMSE_scores,
    'R2': R2_scores,
})

#Mostrar resultados
print(results_df_orig)