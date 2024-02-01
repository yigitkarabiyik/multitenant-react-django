function Get-DirectoryTree {
    param (
        [string]$path,
        [string[]]$excludeFolders,
        [int]$indentLevel = 0
    )

    $indentation = '    ' * $indentLevel

    Get-ChildItem -LiteralPath $path | ForEach-Object {
        if ($excludeFolders -notcontains $_.Name) {
            if ($_.PSIsContainer) {
                Write-Output "$indentation$($_.Name)\"
                Get-DirectoryTree -path $_.FullName -excludeFolders $excludeFolders -indentLevel ($indentLevel + 1)
            } else {
                Write-Output "$indentation$($_.Name)"
            }
        }
    }
}

# Specify the root path and excluded folders
$rootPath = ".\"
$excludeFolders = @("node_modules", "__pycache__", "ven","venv")

# Run the function
Get-DirectoryTree -path $rootPath -excludeFolders $excludeFolders | Out-File tree.txt
