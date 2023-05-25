build:
	go build -o cryptoyank cmd/main.go

run:
	go run main.go

test:
	go test -v ./...

fmt:
	gofmt -l -w .
