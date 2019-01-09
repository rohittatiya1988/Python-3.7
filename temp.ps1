$body = @{“region”=“all”;“request”=“dcip”} | ConvertTo-Json

$webrequest= Invoke-WebRequest -Method “POST” -uri `https://azuredcip.azurewebsites.net/api/azuredcipranges  Jump -Body $body

ConvertFrom-Json -InputObject $webrequest.Content