output "instance_id" {
  value = aws_instance.employee_api.id
}

output "public_ip" {
  value = aws_instance.employee_api.public_ip
}

output "public_dns" {
  value = aws_instance.employee_api.public_dns
}