kubectl get deployments | awk 'NR>1 { print $1 }' | xargs -L1 kubectl delete deployments 
kubectl get services | awk 'NR>1 { print $1 }' | xargs -L1 kubectl delete services 
